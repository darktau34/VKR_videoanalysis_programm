import os

from PyQt6 import QtCore, QtGui, QtWidgets
from PIL import Image, ImageQt

from app_mediaplayer import MediaplayerWindow
from db_processing import select_from_persons
from db_processing import select_from_items, check_items_exists
from db_processing import select_from_emotions_table, check_emotions_exists
from db_processing import select_from_diagramm_table, check_diagramm_exists
from db_processing import select_from_videoclip_table, check_videoclip_exists
from analyze import app_items_detect
from fer_detection import fer_photobox_main, fer_all_frames
from videoprocessing import clip_video_fragment


class DialogWindowMessage(QtWidgets.QDialog):
    def __init__(self, title, msg):
        super().__init__()

        self.setWindowTitle(title)

        QBtn = QtWidgets.QDialogButtonBox.StandardButton.Ok

        self.buttonBox = QtWidgets.QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)

        self.layout = QtWidgets.QVBoxLayout()
        message = QtWidgets.QLabel(msg)
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)


class WorkerSignals(QtCore.QObject):
    """
    Signals from running worker thread
    error signal
    finished signal
    """
    finished = QtCore.pyqtSignal()
    error = QtCore.pyqtSignal(object)


class WorkerVideoclip(QtCore.QObject):
    """
    Worker thread for long tasks (emotion diagramms)
    """
    def __init__(self, func, video_path, person_id, tracker_id):
        super(WorkerVideoclip, self).__init__()
        self.func = func
        self.video_path = video_path
        self.person_id = person_id
        self.tracker_id = tracker_id
        self.signals = WorkerSignals()

    @QtCore.pyqtSlot()
    def run(self):
        self.func(self.video_path, self.person_id, self.tracker_id)
        self.signals.finished.emit()


class WorkerDiag(QtCore.QObject):
    """
    Worker thread for long tasks (emotion diagramms)
    """
    def __init__(self, func, video_path, person_id, tracker_id):
        super(WorkerDiag, self).__init__()
        self.func = func
        self.video_path = video_path
        self.person_id = person_id
        self.tracker_id = tracker_id
        self.signals = WorkerSignals()

    @QtCore.pyqtSlot()
    def run(self):
        self.func(self.video_path, self.person_id, self.tracker_id)
        self.signals.finished.emit()


class WorkerFER(QtCore.QObject):
    """
    Worker thread for long tasks (fer detection)
    """
    def __init__(self, func, photobox_path, person_id):
        super(WorkerFER, self).__init__()
        self.func = func
        self.photobox_path = photobox_path
        self.person_id = person_id
        self.signals = WorkerSignals()

    @QtCore.pyqtSlot()
    def run(self):
        self.func(self.photobox_path, self.person_id)
        self.signals.finished.emit()


class WorkerItems(QtCore.QObject):
    """
    Worker thread for long tasks (items detection)
    """
    def __init__(self, func, person_df, video_path):
        super(WorkerItems, self).__init__()
        self.func = func
        self.video_path = video_path
        self.person_df = person_df
        self.signals = WorkerSignals()

    @QtCore.pyqtSlot()
    def run(self):
        self.func(self.person_df, self.video_path)
        self.signals.finished.emit()


class Ui_analyze(object):
    def __init__(self):
        self.worker_videoclip = None
        self.worker_diag = None
        self.cur_item_num = None
        self.video_id = None
        self.video_path = None
        self.tracker_id = None
        self.main_window = None
        self.videoname = ''
        self.pages_dict = {
            'page_items': 0,
            'page_emotion': 1,
            'page_stats': 2,
            'page_video': 3,
            'page_loading': 4,
            'page_empty': 5
        }
        self.translated_emotions = {
            'angry': 'Злость',
            'sad': 'Грусть',
            'fear': 'Испуг',
            'disgust': 'Отвращение',
            'happy': 'Радость',
            'surprise': 'Удивление',
            'neutral': 'Нейтрально',
            'contempt': 'Презрение'
        }
        self.translated_items = {
            'backpack': 'Рюкзак',
            'umbrella': 'Зонт',
            'handbag': 'Сумка',
            'suitcase': 'Чемодан',
            'baseball_bat': 'Бейсбольная бита',
            'skateboard': 'Скейтборд',
            'bottle': 'Бутылка',
            'knife': 'Нож',
            'laptop': 'Ноутбук',
            'cell_phone': 'Телефон',
            'book': 'Книга',
            'scissors': 'Ножницы'
        }
        self.cur_df_row = None
        self.df_persons = None
        self.cur_photobox_path = None
        self.cur_photobox = None
        self.cur_photobox_pixmap = None
        self.all_btns_list = None
        self.loading_gif = QtGui.QMovie('pyqt_resources/gif_loading.gif')
        self.cur_items_img = None
        self.cur_person_id = None
        self.resources_dir = '/home/slava/projects/nir_7sem/pyqt_resources'

        self.thread = None
        self.worker_items = None

    def setupUi(self, MainWindow, video_id, videoname, video_path):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1037, 529)
        MainWindow.setFixedWidth(1037)
        MainWindow.setFixedHeight(529)
        font = QtGui.QFont()
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(239, 239, 239);")
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.l_photobox = QtWidgets.QLabel(parent=self.centralwidget)
        self.l_photobox.setGeometry(QtCore.QRect(50, 41, 221, 441))
        self.l_photobox.setStyleSheet("background-color: rgb(192, 191, 188);")
        self.l_photobox.setText("")
        self.l_photobox.setObjectName("l_photobox")
        self.btn_photobox_right = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_photobox_right.setEnabled(False)
        self.btn_photobox_right.setGeometry(QtCore.QRect(280, 220, 31, 61))
        self.btn_photobox_right.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 120, 0);\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: rgb(192, 191, 188);\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: qlineargradient(spread:reflect, x1:0.493, y1:0.488545, x2:1, y2:1, stop:0.189055 rgba(255, 120, 0, 255), stop:1 rgba(255, 232, 214, 255));\n"
"}")
        self.btn_photobox_right.setObjectName("btn_photobox_right")
        self.btn_photobox_left = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_photobox_left.setEnabled(False)
        self.btn_photobox_left.setGeometry(QtCore.QRect(10, 220, 31, 61))
        self.btn_photobox_left.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 120, 0);\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: rgb(192, 191, 188);\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: qlineargradient(spread:reflect, x1:0.493, y1:0.488545, x2:1, y2:1, stop:0.189055 rgba(255, 120, 0, 255), stop:1 rgba(255, 232, 214, 255));\n"
"}")
        self.btn_photobox_left.setObjectName("btn_photobox_left")
        self.label_photobox = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_photobox.setGeometry(QtCore.QRect(50, 10, 221, 31))
        self.label_photobox.setStyleSheet("background-color: rgb(255, 120, 0);\n"
"border-color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width: 1px;")
        self.label_photobox.setText("")
        self.label_photobox.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_photobox.setObjectName("label_photobox")
        self.label_appear = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_appear.setGeometry(QtCore.QRect(50, 480, 221, 30))
        self.label_appear.setStyleSheet("background-color: rgba(0, 0, 0, 0.8);\n"
"color: rgb(255, 120, 0);\n"
"")
        self.label_appear.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_appear.setObjectName("label_appear")
        self.btn_items = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_items.setEnabled(True)
        self.btn_items.setGeometry(QtCore.QRect(320, 450, 171, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btn_items.setFont(font)
        self.btn_items.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn_items.setStyleSheet("QPushButton {\n"
"    border-radius: 30px;\n"
"    background-color: rgb(255, 120, 0);\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: rgb(192, 191, 188);\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: qlineargradient(spread:reflect, x1:0.493, y1:0.488545, x2:1, y2:1, stop:0.189055 rgba(255, 120, 0, 255), stop:1 rgba(255, 232, 214, 255));\n"
"}")
        self.btn_items.setObjectName("btn_items")
        self.btn_emotion = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_emotion.setEnabled(True)
        self.btn_emotion.setGeometry(QtCore.QRect(500, 450, 171, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setKerning(True)
        self.btn_emotion.setFont(font)
        self.btn_emotion.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn_emotion.setStyleSheet("QPushButton {\n"
"    border-radius: 30px;\n"
"    background-color: rgb(255, 120, 0);\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: rgb(192, 191, 188);\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: qlineargradient(spread:reflect, x1:0.493, y1:0.488545, x2:1, y2:1, stop:0.189055 rgba(255, 120, 0, 255), stop:1 rgba(255, 232, 214, 255));\n"
"}")
        self.btn_emotion.setObjectName("btn_emotion")
        self.btn_stats = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_stats.setEnabled(True)
        self.btn_stats.setGeometry(QtCore.QRect(680, 450, 171, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btn_stats.setFont(font)
        self.btn_stats.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn_stats.setStyleSheet("QPushButton {\n"
"    border-radius: 30px;\n"
"    background-color: rgb(255, 120, 0);\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: rgb(192, 191, 188);\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: qlineargradient(spread:reflect, x1:0.493, y1:0.488545, x2:1, y2:1, stop:0.189055 rgba(255, 120, 0, 255), stop:1 rgba(255, 232, 214, 255));\n"
"}")
        self.btn_stats.setObjectName("btn_stats")
        self.btn_video = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_video.setEnabled(True)
        self.btn_video.setGeometry(QtCore.QRect(860, 450, 171, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btn_video.setFont(font)
        self.btn_video.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn_video.setStyleSheet("QPushButton {\n"
"    border-radius: 30px;\n"
"    background-color: rgb(255, 120, 0);\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: rgb(192, 191, 188);\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: qlineargradient(spread:reflect, x1:0.493, y1:0.488545, x2:1, y2:1, stop:0.189055 rgba(255, 120, 0, 255), stop:1 rgba(255, 232, 214, 255));\n"
"}")
        self.btn_video.setObjectName("btn_video")
        self.stackedWidget = QtWidgets.QStackedWidget(parent=self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(320, 10, 701, 431))
        self.stackedWidget.setStyleSheet("background-color: rgb(222, 221, 218);")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_items = QtWidgets.QWidget()
        self.page_items.setObjectName("page_items")
        self.l_show_item = QtWidgets.QLabel(parent=self.page_items)
        self.l_show_item.setGeometry(QtCore.QRect(400, 40, 271, 381))
        self.l_show_item.setStyleSheet("background-color: rgb(119, 118, 123);\n"
"border-color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"")
        self.l_show_item.setText("")
        self.l_show_item.setObjectName("l_show_item")
        self.label_show_item = QtWidgets.QLabel(parent=self.page_items)
        self.label_show_item.setGeometry(QtCore.QRect(400, 10, 271, 31))
        self.label_show_item.setStyleSheet("background-color: rgb(255, 120, 0);\n"
"border-color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width: 2px;")
        self.label_show_item.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_show_item.setObjectName("label_show_item")
        self.list_view_items = QtWidgets.QListWidget(parent=self.page_items)
        self.list_view_items.setEnabled(True)
        self.list_view_items.setGeometry(QtCore.QRect(20, 40, 241, 381))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferDefault)
        self.list_view_items.setFont(font)
        self.list_view_items.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.list_view_items.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.list_view_items.setStyleSheet("QListView{\n"
"    background-color: rgb(119, 118, 123);\n"
"    border-color: rgb(0, 0, 0);\n"
"    border-style: solid;\n"
"    border-width: 2px;\n"
"    padding: 5px;\n"
"    padding-left: 5px;\n"
"}\n"
"\n"
"QListView:item{\n"
"    border: 2px solid black;\n"
"    background-color: rgb(192, 191, 188);\n"
"    margin:10px;\n"
"    height:50px;\n"
"    width:200px;\n"
"}\n"
"\n"
"QListView:item:selected{\n"
"    border: 1px solid black;\n"
"    background-color: rgba(255, 120, 0, 171);\n"
"}")
        self.list_view_items.setAutoScroll(True)
        self.list_view_items.setMovement(QtWidgets.QListView.Movement.Static)
        self.list_view_items.setFlow(QtWidgets.QListView.Flow.LeftToRight)
        self.list_view_items.setProperty("isWrapping", True)
        self.list_view_items.setResizeMode(QtWidgets.QListView.ResizeMode.Fixed)
        self.list_view_items.setLayoutMode(QtWidgets.QListView.LayoutMode.SinglePass)
        self.list_view_items.setGridSize(QtCore.QSize(120, 60))
        self.list_view_items.setViewMode(QtWidgets.QListView.ViewMode.ListMode)
        self.list_view_items.setModelColumn(0)
        self.list_view_items.setUniformItemSizes(False)
        self.list_view_items.setWordWrap(False)
        self.list_view_items.setSelectionRectVisible(True)
        self.list_view_items.setObjectName("list_view_items")
        item = QtWidgets.QListWidgetItem()
        self.list_view_items.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list_view_items.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list_view_items.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list_view_items.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list_view_items.addItem(item)
        self.label_items = QtWidgets.QLabel(parent=self.page_items)
        self.label_items.setGeometry(QtCore.QRect(20, 10, 241, 31))
        self.label_items.setStyleSheet("background-color: rgb(255, 120, 0);\n"
"border-color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width: 2px;")
        self.label_items.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_items.setObjectName("label_items")
        self.stackedWidget.addWidget(self.page_items)
        self.page_emotion = QtWidgets.QWidget()
        self.page_emotion.setObjectName("page_emotion")
        self.l_facebox = QtWidgets.QLabel(parent=self.page_emotion)
        self.l_facebox.setGeometry(QtCore.QRect(20, 40, 221, 381))
        self.l_facebox.setStyleSheet("background-color: rgb(119, 118, 123);\n"
"border-color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width: 2px;")
        self.l_facebox.setText("")
        self.l_facebox.setObjectName("l_facebox")
        self.label_facebox = QtWidgets.QLabel(parent=self.page_emotion)
        self.label_facebox.setGeometry(QtCore.QRect(20, 10, 221, 31))
        self.label_facebox.setStyleSheet("background-color: rgb(255, 120, 0);\n"
"border-color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width: 2px;")
        self.label_facebox.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_facebox.setObjectName("label_facebox")
        self.list_view_emotions = QtWidgets.QListWidget(parent=self.page_emotion)
        self.list_view_emotions.setEnabled(True)
        self.list_view_emotions.setGeometry(QtCore.QRect(260, 40, 191, 381))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferDefault)
        self.list_view_emotions.setFont(font)
        self.list_view_emotions.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.list_view_emotions.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.list_view_emotions.setStyleSheet("QListView{\n"
"    background-color: rgb(119, 118, 123);\n"
"    border-color: rgb(0, 0, 0);\n"
"    border-style: solid;\n"
"    border-width: 2px;\n"
"    padding: 0px;\n"
"    padding-left: 0px;\n"
"    padding-bottom: 0px;\n"
"}\n"
"\n"
"QListView:item{\n"
"    border: 2px solid black;\n"
"    background-color: rgb(192, 191, 188);\n"
"    margin:6px;\n"
"    height:45px;\n"
"    width:170px;\n"
"}\n"
"\n"
"QListView:item:selected{\n"
"    border: 1px solid black;\n"
"    background-color: rgba(255, 120, 0, 171);\n"
"}")
        self.list_view_emotions.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.list_view_emotions.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.list_view_emotions.setAutoScroll(True)
        self.list_view_emotions.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.NoSelection)
        self.list_view_emotions.setMovement(QtWidgets.QListView.Movement.Static)
        self.list_view_emotions.setFlow(QtWidgets.QListView.Flow.LeftToRight)
        self.list_view_emotions.setProperty("isWrapping", True)
        self.list_view_emotions.setResizeMode(QtWidgets.QListView.ResizeMode.Fixed)
        self.list_view_emotions.setLayoutMode(QtWidgets.QListView.LayoutMode.SinglePass)
        self.list_view_emotions.setGridSize(QtCore.QSize(120, 53))
        self.list_view_emotions.setViewMode(QtWidgets.QListView.ViewMode.ListMode)
        self.list_view_emotions.setModelColumn(0)
        self.list_view_emotions.setUniformItemSizes(False)
        self.list_view_emotions.setWordWrap(False)
        self.list_view_emotions.setSelectionRectVisible(True)
        self.list_view_emotions.setObjectName("list_view_emotions")
        item = QtWidgets.QListWidgetItem()
        self.list_view_emotions.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list_view_emotions.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list_view_emotions.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list_view_emotions.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list_view_emotions.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list_view_emotions.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list_view_emotions.addItem(item)
        self.label_emotions = QtWidgets.QLabel(parent=self.page_emotion)
        self.label_emotions.setGeometry(QtCore.QRect(260, 10, 191, 31))
        self.label_emotions.setStyleSheet("background-color: rgb(255, 120, 0);\n"
"border-color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width: 2px;")
        self.label_emotions.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_emotions.setObjectName("label_emotions")
        self.label_emotionbox = QtWidgets.QLabel(parent=self.page_emotion)
        self.label_emotionbox.setGeometry(QtCore.QRect(470, 90, 211, 31))
        self.label_emotionbox.setStyleSheet("background-color: rgb(255, 120, 0);\n"
"border-color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width: 2px;")
        self.label_emotionbox.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_emotionbox.setObjectName("label_emotionbox")
        self.l_emotionbox = QtWidgets.QLabel(parent=self.page_emotion)
        self.l_emotionbox.setGeometry(QtCore.QRect(500, 140, 151, 141))
        self.l_emotionbox.setStyleSheet("background-color: rgb(119, 118, 123);\n"
"")
        self.l_emotionbox.setText("")
        self.l_emotionbox.setPixmap(QtGui.QPixmap("pyqt_resources/icon_neutral.png"))
        self.l_emotionbox.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.l_emotionbox.setObjectName("l_emotionbox")
        self.label_emotionname = QtWidgets.QLabel(parent=self.page_emotion)
        self.label_emotionname.setGeometry(QtCore.QRect(470, 120, 211, 191))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label_emotionname.setFont(font)
        self.label_emotionname.setStyleSheet("background-color: rgb(119, 118, 123);\n"
"color: rgb(255, 120, 0);\n"
"border-color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width: 2px;")
        self.label_emotionname.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.label_emotionname.setObjectName("label_emotionname")
        self.l_facebox.raise_()
        self.label_facebox.raise_()
        self.list_view_emotions.raise_()
        self.label_emotions.raise_()
        self.label_emotionbox.raise_()
        self.label_emotionname.raise_()
        self.l_emotionbox.raise_()
        self.stackedWidget.addWidget(self.page_emotion)
        self.page_stats = QtWidgets.QWidget()
        self.page_stats.setObjectName("page_stats")
        self.l_statsbox = QtWidgets.QLabel(parent=self.page_stats)
        self.l_statsbox.setGeometry(QtCore.QRect(10, 10, 681, 411))
        self.l_statsbox.setStyleSheet("background-color: rgb(119, 118, 123);\n"
"border-color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width: 2px;")
        self.l_statsbox.setText("")
        self.l_statsbox.setObjectName("l_statsbox")
        self.stackedWidget.addWidget(self.page_stats)
        self.page_video = QtWidgets.QWidget()
        self.page_video.setObjectName("page_video")
        self.stackedWidget.addWidget(self.page_video)
        self.btn_show_video = QtWidgets.QPushButton(parent=self.page_video)
        self.btn_show_video.setEnabled(False)
        self.btn_show_video.setGeometry(QtCore.QRect(260, 175, 200, 100))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setKerning(True)
        self.btn_show_video.setFont(font)
        self.btn_show_video.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn_show_video.setStyleSheet("QPushButton {\n"
                                       "    border-radius: 30px;\n"
                                       "    background-color: rgb(255, 120, 0);\n"
                                       "    border-style: solid;\n"
                                       "    border-width: 1px;\n"
                                       "    border-color: rgb(0, 0, 0);\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:disabled {\n"
                                       "    background-color: rgb(192, 191, 188);\n"
                                       "    color: rgb(0, 0, 0);\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:hover {\n"
                                       "    background-color: qlineargradient(spread:reflect, x1:0.493, y1:0.488545, x2:1, y2:1, stop:0.189055 rgba(255, 120, 0, 255), stop:1 rgba(255, 232, 214, 255));\n"
                                       "}")
        self.btn_show_video.setObjectName("btn_show_video")
        self.page_loading = QtWidgets.QWidget()
        self.page_loading.setObjectName("page_loading")
        self.l_loading = QtWidgets.QLabel(parent=self.page_loading)
        self.l_loading.setGeometry(QtCore.QRect(210, 220, 301, 41))
        self.l_loading.setStyleSheet("")
        self.l_loading.setText("")
        self.l_loading.setObjectName("l_loading")
        self.label_loading = QtWidgets.QLabel(parent=self.page_loading)
        self.label_loading.setGeometry(QtCore.QRect(250, 180, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_loading.setFont(font)
        self.label_loading.setStyleSheet("")
        self.label_loading.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_loading.setObjectName("label_loading")
        self.stackedWidget.addWidget(self.page_loading)
        self.page_empty = QtWidgets.QWidget()
        self.page_empty.setObjectName("page_empty")
        self.stackedWidget.addWidget(self.page_empty)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        self.list_view_items.setCurrentRow(-1)
        self.list_view_emotions.setCurrentRow(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.video_id = video_id
        self.video_path = video_path
        self.videoname = videoname
        MainWindow.setWindowTitle(f'Анализ людей - {videoname}')
        self.my_setup()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Анализ людей"))
        self.btn_photobox_right.setText(_translate("MainWindow", ">"))
        self.btn_photobox_left.setText(_translate("MainWindow", "<"))
        self.label_appear.setText(_translate("MainWindow", "Время появления: 00:00:00"))
        self.btn_items.setText(_translate("MainWindow", "Распознавание\n"
"предметов"))
        self.btn_emotion.setText(_translate("MainWindow", "Распознавание\n"
"текущей эмоции"))
        self.btn_stats.setText(_translate("MainWindow", "Диаграмма эмоций\n"
"по всем кадрам"))
        self.btn_video.setText(_translate("MainWindow", "Отрывок видео\n"
"с человеком"))
        self.btn_show_video.setText(_translate("MainWindow", "Показать\nвидео"))
        self.label_show_item.setText(_translate("MainWindow", "Просмотр предмета"))
        self.list_view_items.setSortingEnabled(False)
        __sortingEnabled = self.list_view_items.isSortingEnabled()
        self.list_view_items.setSortingEnabled(False)
        item = self.list_view_items.item(0)
        item.setText(_translate("MainWindow", "New Item - 30%"))
        item = self.list_view_items.item(1)
        item.setText(_translate("MainWindow", "New Item"))
        item = self.list_view_items.item(2)
        item.setText(_translate("MainWindow", "New Item"))
        item = self.list_view_items.item(3)
        item.setText(_translate("MainWindow", "New Item"))
        item = self.list_view_items.item(4)
        item.setText(_translate("MainWindow", "New Item"))
        self.list_view_items.setSortingEnabled(__sortingEnabled)
        self.label_items.setText(_translate("MainWindow", "Предметы"))
        self.label_facebox.setText(_translate("MainWindow", "Обнаруженное лицо"))
        self.list_view_emotions.setSortingEnabled(False)
        __sortingEnabled = self.list_view_emotions.isSortingEnabled()
        self.list_view_emotions.setSortingEnabled(False)
        item = self.list_view_emotions.item(0)
        item.setText(_translate("MainWindow", "Злость - 69%"))
        item = self.list_view_emotions.item(1)
        item.setText(_translate("MainWindow", "Грусть - 0%"))
        item = self.list_view_emotions.item(2)
        item.setText(_translate("MainWindow", "Отвращение - 0%"))
        item = self.list_view_emotions.item(3)
        item.setText(_translate("MainWindow", "Испуг - 8%"))
        item = self.list_view_emotions.item(4)
        item.setText(_translate("MainWindow", "Радость - 34%"))
        item = self.list_view_emotions.item(5)
        item.setText(_translate("MainWindow", "Удивление - 0%"))
        item = self.list_view_emotions.item(6)
        item.setText(_translate("MainWindow", "Нейтрально - 29%"))
        self.list_view_emotions.setSortingEnabled(__sortingEnabled)
        self.label_emotions.setText(_translate("MainWindow", "Распознанные эмоции"))
        self.label_emotionbox.setText(_translate("MainWindow", "Преобладающая эмоция"))
        self.label_emotionname.setText(_translate("MainWindow", "Нейтрально"))
        self.label_loading.setText(_translate("MainWindow", "Загрузка"))

    def my_setup(self):
        self.stackedWidget.setCurrentIndex(self.pages_dict.get('page_empty'))

        self.df_persons = select_from_persons(self.video_id)

        self.cur_df_row = 0
        first_person = self.df_persons.iloc[self.cur_df_row]
        self.cur_person_id = first_person.person_id
        self.tracker_id = first_person.tracker_id
        # Устанавливаем картинку в фотобокс для 1-го человека
        self.add_photobox(first_person)
        # Устанавливаем все labels для 1-го
        self.add_labels(first_person)

        # Активируем кнопку
        if len(self.df_persons) > 1:
            self.btn_photobox_right.setEnabled(True)

        self.btn_photobox_right.clicked.connect(self.person_to_right)
        self.btn_photobox_left.clicked.connect(self.person_to_left)
        self.btn_items.clicked.connect(self.start_items_recognition)
        self.btn_emotion.clicked.connect(self.start_emotion_recognition)
        self.btn_stats.clicked.connect(self.start_diagramms)
        self.btn_video.clicked.connect(self.start_videoclip)
        self.btn_show_video.clicked.connect(self.show_videoclip)
        self.list_view_items.currentRowChanged.connect(self.items_currentRowChanged_handler)

        self.l_loading.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.l_loading.setMovie(self.loading_gif)

        self.all_btns_list = [self.btn_items, self.btn_emotion, self.btn_stats, self.btn_video, self.btn_photobox_right, self.btn_photobox_left]

    def show_videoclip(self):
        videoclip_path = select_from_videoclip_table(self.cur_person_id)
        self.mediaplayer_window = QtWidgets.QMainWindow()
        self.mediaplayer_ui = MediaplayerWindow()
        self.mediaplayer_ui.setupUI(self.mediaplayer_window, videoclip_path)
        self.mediaplayer_window.show()

    def videoclip_finished(self):
        for btn in self.all_btns_list:
            btn.setEnabled(True)

        self.loading_gif.stop()
        self.stackedWidget.setCurrentIndex(self.pages_dict.get('page_video'))
        self.btn_show_video.setEnabled(True)

    def start_videoclip(self):
        if not check_videoclip_exists(self.cur_person_id):
            for btn in self.all_btns_list:
                btn.setEnabled(False)

            self.stackedWidget.setCurrentIndex(self.pages_dict.get('page_loading'))
            self.loading_gif.start()

            self.thread = QtCore.QThread()
            self.worker_videoclip = WorkerVideoclip(clip_video_fragment, self.video_path, self.cur_person_id, self.tracker_id)

            self.worker_videoclip.moveToThread(self.thread)
            self.worker_videoclip.signals.finished.connect(self.videoclip_finished)
            self.worker_videoclip.signals.finished.connect(self.thread.quit)
            self.worker_videoclip.signals.finished.connect(self.worker_videoclip.deleteLater)

            self.thread.started.connect(self.worker_videoclip.run)
            self.thread.finished.connect(self.thread.deleteLater)
            self.thread.start()
        else:
            self.stackedWidget.setCurrentIndex(self.pages_dict.get('page_video'))
            self.btn_show_video.setEnabled(True)


    def add_diagramm(self):
        self.l_statsbox.clear()

        diagramm_path = select_from_diagramm_table(self.cur_person_id)
        diagramm = self.resize_image(diagramm_path, self.l_statsbox)
        diagramm_pixmap = QtGui.QPixmap(diagramm)
        self.l_statsbox.setPixmap(diagramm_pixmap)


    def diagramms_finished(self):
        for btn in self.all_btns_list:
            btn.setEnabled(True)

        self.loading_gif.stop()
        self.stackedWidget.setCurrentIndex(self.pages_dict.get('page_stats'))
        self.add_diagramm()

    def start_diagramms(self):
        if not check_diagramm_exists(self.cur_person_id):
            for btn in self.all_btns_list:
                btn.setEnabled(False)

            self.stackedWidget.setCurrentIndex(self.pages_dict.get('page_loading'))
            self.loading_gif.start()

            self.thread = QtCore.QThread()
            self.worker_diag = WorkerDiag(fer_all_frames, self.video_path, self.cur_person_id, self.tracker_id)

            self.worker_diag.moveToThread(self.thread)
            self.worker_diag.signals.finished.connect(self.diagramms_finished)
            self.worker_diag.signals.finished.connect(self.thread.quit)
            self.worker_diag.signals.finished.connect(self.worker_diag.deleteLater)

            self.thread.started.connect(self.worker_diag.run)
            self.thread.finished.connect(self.thread.deleteLater)
            self.thread.start()
        else:
            self.stackedWidget.setCurrentIndex(self.pages_dict.get('page_stats'))
            self.add_diagramm()



    def add_emotion(self):
        self.list_view_emotions.clear()
        self.l_facebox.clear()
        self.l_emotionbox.clear()
        self.label_emotionname.clear()

        emotion = select_from_emotions_table(self.cur_person_id)

        if emotion:
            facebox_path = emotion[0]
            emotion_dict = emotion[1]
            top_emotion = emotion[2]
            need_warning = emotion[3]

            # устанавливаем facebox
            cur_facebox = self.resize_image(facebox_path, self.l_facebox)
            cur_facebox_pixmap = QtGui.QPixmap(cur_facebox)
            self.l_facebox.setPixmap(cur_facebox_pixmap)

            # добавляем айтемы
            for emotion in emotion_dict:
                em_value = int(emotion_dict.get(emotion) * 100)
                emotion_translated = self.translated_emotions.get(emotion)
                item = QtWidgets.QListWidgetItem(emotion_translated + ' - ' + str(em_value) + '%')
                self.list_view_emotions.addItem(item)

            # устанавливаем преобладающую эмоцию

            for icon in os.listdir(self.resources_dir):
                icon_splitted = icon.split('_')[-1]
                icon_splitted = icon_splitted.split('.')[0]
                if icon_splitted == top_emotion:
                    icon_path = os.path.join(self.resources_dir, icon)
                    icon_pixmap = QtGui.QPixmap(icon_path)
                    self.l_emotionbox.setPixmap(icon_pixmap)
                    break

            emotion_translated = self.translated_emotions.get(top_emotion)
            self.label_emotionname.setText(emotion_translated)

            # модальное окно предупреждения о том, что лицо маленькое (< 48*48)
            if need_warning:
                dlg = DialogWindowMessage('Предупреждение', 'Обнаруженное лицо маленького размера,\nВозможно неправильное распознавание эмоции')
                dlg.exec()
        else:
            self.list_view_emotions.clear()
            self.l_facebox.clear()
            self.l_emotionbox.clear()
            self.label_emotionname.clear()

            # вывести модальное окно - эмоция не обнаружена
            dlg = DialogWindowMessage('Программа', 'Лицо не было обнаружено')
            dlg.exec()


    def emotion_recognition_finished(self):
        for btn in self.all_btns_list:
            btn.setEnabled(True)

        self.loading_gif.stop()
        self.stackedWidget.setCurrentIndex(self.pages_dict.get('page_emotion'))

        self.add_emotion()

    def start_emotion_recognition(self):
        if not check_emotions_exists(self.cur_person_id):
            for btn in self.all_btns_list:
                btn.setEnabled(False)

            self.stackedWidget.setCurrentIndex(self.pages_dict.get('page_loading'))
            self.loading_gif.start()

            self.thread = QtCore.QThread()
            self.worker_items = WorkerFER(fer_photobox_main, self.cur_photobox_path, self.cur_person_id)

            self.worker_items.moveToThread(self.thread)
            self.worker_items.signals.finished.connect(self.emotion_recognition_finished)
            self.worker_items.signals.finished.connect(self.thread.quit)
            self.worker_items.signals.finished.connect(self.worker_items.deleteLater)

            self.thread.started.connect(self.worker_items.run)
            self.thread.finished.connect(self.thread.deleteLater)
            self.thread.start()
        else:
            self.stackedWidget.setCurrentIndex(self.pages_dict.get('page_emotion'))
            self.add_emotion()


    def items_currentRowChanged_handler(self):
        self.cur_item_num = self.list_view_items.currentRow()
        img_path = self.cur_items_img[self.cur_item_num]
        cur_img = self.resize_image(img_path, self.l_show_item)
        cur_img_pixmap = QtGui.QPixmap(cur_img)
        self.l_show_item.setPixmap(cur_img_pixmap)

    def add_items(self):
        self.list_view_items.clear()
        self.l_show_item.clear()
        df_items = select_from_items(self.cur_person_id)
        self.cur_items_img = []
        if not df_items.empty:
            for item_row in df_items.iterrows():
                item_name = item_row[1].item_name
                conf = item_row[1].confidence
                item_img = item_row[1].item_photo
                self.cur_items_img.append(item_img)
                item = QtWidgets.QListWidgetItem(self.translated_items[item_name] + ' - ' + str(conf) + '%')
                self.list_view_items.addItem(item)

    def items_recognition_finished(self):
        for btn in self.all_btns_list:
            btn.setEnabled(True)

        self.loading_gif.stop()
        self.stackedWidget.setCurrentIndex(self.pages_dict.get('page_items'))
        self.add_items()

    def start_items_recognition(self):
        if not check_items_exists(self.cur_person_id):
            for btn in self.all_btns_list:
                btn.setEnabled(False)

            self.stackedWidget.setCurrentIndex(self.pages_dict.get('page_loading'))
            self.loading_gif.start()

            person_df = self.df_persons.iloc[self.cur_df_row]

            self.thread = QtCore.QThread()
            self.worker_items = WorkerItems(app_items_detect, person_df, self.video_path)

            self.worker_items.moveToThread(self.thread)
            self.worker_items.signals.finished.connect(self.items_recognition_finished)
            self.worker_items.signals.finished.connect(self.thread.quit)
            self.worker_items.signals.finished.connect(self.worker_items.deleteLater)

            self.thread.started.connect(self.worker_items.run)
            self.thread.finished.connect(self.thread.deleteLater)
            self.thread.start()
        else:
            self.stackedWidget.setCurrentIndex(self.pages_dict.get('page_items'))
            self.add_items()

    def person_changed(self, df_row):
        self.add_photobox(df_row)
        self.add_labels(df_row)
        self.stackedWidget.setCurrentIndex(self.pages_dict.get('page_empty'))
        self.cur_person_id = df_row.person_id
        self.tracker_id = df_row.tracker_id

    def person_to_right(self):
        max_row = len(self.df_persons) - 1
        if self.cur_df_row != max_row:
            self.cur_df_row += 1
        if self.cur_df_row == max_row:
            self.btn_photobox_right.setEnabled(False)

        self.btn_photobox_left.setEnabled(True)

        person_df = self.df_persons.iloc[self.cur_df_row]
        self.person_changed(person_df)

    def person_to_left(self):
        min_row = 0
        if self.cur_df_row != min_row:
            self.cur_df_row -= 1
        if self.cur_df_row == min_row:
            self.btn_photobox_left.setEnabled(False)

        self.btn_photobox_right.setEnabled(True)
        person_df = self.df_persons.iloc[self.cur_df_row]
        self.person_changed(person_df)

    def add_labels(self, df_row):
        photobox_label = "Человек: " + str(df_row.ui_tracker_id)
        self.label_photobox.setText(photobox_label)
        self.label_appear.setText('Время появления: ' + df_row.appear_time)

    def add_photobox(self, df_row):
        self.cur_photobox_path = df_row.photobox
        self.cur_photobox = self.resize_image(self.cur_photobox_path, self.l_photobox)
        self.cur_photobox_pixmap = QtGui.QPixmap(self.cur_photobox)
        self.l_photobox.setPixmap(self.cur_photobox_pixmap)

    def resize_image(self, img_path, l_imgbox):
        img = Image.open(img_path)
        fixed_width = l_imgbox.width()
        fixed_height = l_imgbox.height()
        new_image = img.resize((fixed_width, fixed_height))
        new_img = ImageQt.toqpixmap(new_image).copy()
        return new_img


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_analyze()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
