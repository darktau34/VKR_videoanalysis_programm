import os
import sys
import logging
import cv2 as cv
from PyQt6 import QtCore, QtGui, QtWidgets
from PIL import Image, ImageQt

from analyze import app_analyze
from app_analysis import Ui_analyze
from db_processing import check_video_db_exists_bypath

LOG_FORMAT = '%(asctime)s [%(levelname)s] %(name)s %(funcName)s %(lineno)d: %(message)s'
DATE_FORMAT = '%H:%M:%S'
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT, datefmt=DATE_FORMAT)


class WorkerSignals(QtCore.QObject):
    """
    Signals from running worker thread
    error signal
    finished signal
    """
    finished = QtCore.pyqtSignal()
    error = QtCore.pyqtSignal(object)


class Worker(QtCore.QObject):
    """
    Worker thread for long tasks
    """

    def __init__(self, func, video_path, appear_time, progress_bar):
        super(Worker, self).__init__()
        self.func = func
        self.video_path = video_path
        self.appear_time = appear_time
        self.progress_bar = progress_bar
        self.signals = WorkerSignals()

    @QtCore.pyqtSlot()
    def run(self):
        try:
            self.func(self.video_path, self.appear_time, self.progress_bar)
        except Exception as e:
            self.signals.error.emit(e)
        finally:
            self.signals.finished.emit()



class Ui_MainWindow(object):
    def __init__(self):
        self.appear_time = ''
        self.video_id = None
        self.video_path = None
        self.videos_dir = ''
        self.video_list = []
        self.video_icon = QtGui.QIcon('pyqt_resources/video_icon.png')
        self.cur_video = None
        self.cur_video_num = None
        self.cur_video_preview = None

        # self.threadpool = QtCore.QThreadPool()
        # self.threadpool.setMaxThreadCount(1)
        # logger.info("Multithreading with maximum %d threads", self.threadpool.maxThreadCount())

        self.thread = None
        self.worker = None

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1280, 698)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        MainWindow.setFont(font)
        MainWindow.setMouseTracking(False)
        MainWindow.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        MainWindow.setStyleSheet("background-color: rgb(239, 239, 239);")
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.list_view = QtWidgets.QListWidget(parent=self.centralwidget)
        self.list_view.setGeometry(QtCore.QRect(10, 30, 301, 661))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.list_view.setFont(font)
        self.list_view.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.list_view.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.list_view.setStyleSheet("QListView{\n"
"    background-color: rgb(192, 191, 188);\n"
"    border-color: rgb(0, 0, 0);\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    padding: 5px;\n"
"    padding-left: 5px;\n"
"}\n"
"\n"
"QListView:item{\n"
"    border: 2px solid black;\n"
"    margin:5px;\n"
"    height:60px;\n"
"    width:255px;\n"
"}\n"
"\n"
"QListView:item:selected{\n"
"    border: 1px solid black;\n"
"    background-color: rgba(255, 120, 0, 171);\n"
"}")
        self.list_view.setAutoScroll(True)
        self.list_view.setIconSize(QtCore.QSize(35, 35))
        self.list_view.setMovement(QtWidgets.QListView.Movement.Static)
        self.list_view.setFlow(QtWidgets.QListView.Flow.LeftToRight)
        self.list_view.setProperty("isWrapping", True)
        self.list_view.setResizeMode(QtWidgets.QListView.ResizeMode.Fixed)
        self.list_view.setLayoutMode(QtWidgets.QListView.LayoutMode.SinglePass)
        self.list_view.setGridSize(QtCore.QSize(200, 70))
        self.list_view.setViewMode(QtWidgets.QListView.ViewMode.ListMode)
        self.list_view.setModelColumn(0)
        self.list_view.setUniformItemSizes(False)
        self.list_view.setWordWrap(False)
        self.list_view.setSelectionRectVisible(True)
        self.list_view.setObjectName("list_view")
        item = QtWidgets.QListWidgetItem()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("pyqt_resources/video_icon.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        item.setIcon(icon)
        self.list_view.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list_view.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list_view.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list_view.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list_view.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list_view.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list_view.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list_view.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list_view.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list_view.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list_view.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list_view.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list_view.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list_view.addItem(item)
        self.l_videos = QtWidgets.QLabel(parent=self.centralwidget)
        self.l_videos.setGeometry(QtCore.QRect(10, 0, 241, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.l_videos.setFont(font)
        self.l_videos.setStyleSheet("background-color: rgb(255, 120, 0);\n"
"border-color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"")
        self.l_videos.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.l_videos.setObjectName("l_videos")
        self.l_preview = QtWidgets.QLabel(parent=self.centralwidget)
        self.l_preview.setGeometry(QtCore.QRect(340, 30, 901, 491))
        self.l_preview.setStyleSheet("background-color: rgb(192, 191, 188);\n"
"border-color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width: 1px;")
        self.l_preview.setText("")
        self.l_preview.setObjectName("l_preview")
        self.btn_analyze = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_analyze.setEnabled(False)
        self.btn_analyze.setGeometry(QtCore.QRect(340, 540, 591, 61))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 120, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 120, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 120, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.BrushStyle.NoBrush)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 120, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 120, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 120, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.BrushStyle.NoBrush)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(192, 191, 188))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(192, 191, 188))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(192, 191, 188))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.PlaceholderText, brush)
        self.btn_analyze.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.btn_analyze.setFont(font)
        self.btn_analyze.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn_analyze.setStyleSheet("QPushButton {\n"
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
        self.btn_analyze.setObjectName("btn_analyze")
        self.btn_prev = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_prev.setEnabled(False)
        self.btn_prev.setGeometry(QtCore.QRect(940, 540, 301, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.btn_prev.setFont(font)
        self.btn_prev.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn_prev.setStyleSheet("QPushButton {\n"
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
        self.btn_prev.setObjectName("btn_prev")
        self.progress_bar = QtWidgets.QProgressBar(parent=self.centralwidget)
        self.progress_bar.setEnabled(True)
        self.progress_bar.setGeometry(QtCore.QRect(340, 640, 591, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(192, 191, 188))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(192, 191, 188))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(192, 191, 188))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.BrushStyle.NoBrush)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(192, 191, 188))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(192, 191, 188))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(192, 191, 188))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.BrushStyle.NoBrush)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 239, 239))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 239, 239))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 239, 239))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 239, 239))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 239, 239))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 239, 239))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 239, 239))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.PlaceholderText, brush)
        self.progress_bar.setPalette(palette)
        self.progress_bar.setStyleSheet("QProgressBar {\n"
"    background-color: rgb(192, 191, 188);\n"
"    border: 2px solid grey;\n"
"    border-radius: 10px;\n"
"    text-align: center;\n"
"    padding-left:4px;\n"
"    padding-right:4px;\n"
"}\n"
"\n"
"QProgressBar:chunk {\n"
"    background-color: rgb(255, 120, 0);\n"
"    width: 10px;\n"
"    margin: 1px;\n"
"}\n"
"\n"
"QProgressBar:disabled {\n"
"    background-color: rgb(239, 239, 239);\n"
"    border: 2px solid rgb(239, 239, 239);\n"
"    color: rgb(239, 239, 239);\n"
"}\n"
"")
        self.progress_bar.setProperty("value", 0)
        self.progress_bar.setTextVisible(True)
        self.progress_bar.setInvertedAppearance(False)
        self.progress_bar.setObjectName("progress_bar")
        self.l_videoname = QtWidgets.QLabel(parent=self.centralwidget)
        self.l_videoname.setGeometry(QtCore.QRect(350, 7, 881, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.l_videoname.setFont(font)
        self.l_videoname.setText("")
        self.l_videoname.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.l_videoname.setObjectName("l_videoname")
        self.l_appear = QtWidgets.QLabel(parent=self.centralwidget)
        self.l_appear.setGeometry(QtCore.QRect(940, 640, 301, 31))
        self.l_appear.setStyleSheet("border-color: rgb(154, 153, 150);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"background-color: rgb(255, 120, 0);")
        self.l_appear.setObjectName("l_appear")
        self.input_appear = QtWidgets.QTimeEdit(parent=self.centralwidget)
        self.input_appear.setGeometry(QtCore.QRect(1102, 640, 139, 31))
        font = QtGui.QFont()
        font.setBold(True)
        self.input_appear.setFont(font)
        self.input_appear.setStyleSheet("background-color: rgb(192, 191, 188);\n"
"color: rgb(230, 97, 0);\n"
"border-color: rgb(0, 0, 0);\n"
"\n"
"")
        self.input_appear.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.input_appear.setObjectName("input_appear")
        self.btn_dir = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_dir.setGeometry(QtCore.QRect(250, 0, 31, 31))
        self.btn_dir.setStyleSheet("QPushButton {\n"
"    border-radius: 30px;\n"
"    background-color: rgb(119, 118, 123);\n"
"    border-style: solid;\n"
"    border-width: 2px;\n"
"    border-color: rgb(0, 0, 0);\n"
"}")
        self.btn_dir.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("pyqt_resources/icon_directory.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_dir.setIcon(icon1)
        self.btn_dir.setIconSize(QtCore.QSize(21, 21))
        self.btn_dir.setCheckable(False)
        self.btn_dir.setObjectName("btn_dir")
        self.btn_refresh = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_refresh.setGeometry(QtCore.QRect(280, 0, 31, 31))
        self.btn_refresh.setStyleSheet("QPushButton {\n"
"    border-radius: 30px;\n"
"    background-color: rgb(119, 118, 123);\n"
"    border-style: solid;\n"
"    border-width: 2px;\n"
"    border-color: rgb(0, 0, 0);\n"
"}")
        self.btn_refresh.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("pyqt_resources/icon_refresh.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_refresh.setIcon(icon2)
        self.btn_refresh.setIconSize(QtCore.QSize(21, 21))
        self.btn_refresh.setObjectName("btn_refresh")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.list_view.setCurrentRow(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.mySetupUI()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Анализ людей на видеозаписи"))
        self.list_view.setSortingEnabled(False)
        __sortingEnabled = self.list_view.isSortingEnabled()
        self.list_view.setSortingEnabled(False)
        item = self.list_view.item(0)
        item.setText(_translate("MainWindow", "New Item New Item New Item"))
        item = self.list_view.item(1)
        item.setText(_translate("MainWindow", "New Item"))
        item = self.list_view.item(2)
        item.setText(_translate("MainWindow", "New Item"))
        item = self.list_view.item(3)
        item.setText(_translate("MainWindow", "New Item"))
        item = self.list_view.item(4)
        item.setText(_translate("MainWindow", "New Item"))
        item = self.list_view.item(5)
        item.setText(_translate("MainWindow", "New Item"))
        item = self.list_view.item(6)
        item.setText(_translate("MainWindow", "New Item"))
        item = self.list_view.item(7)
        item.setText(_translate("MainWindow", "New Item"))
        item = self.list_view.item(8)
        item.setText(_translate("MainWindow", "New Item"))
        item = self.list_view.item(9)
        item.setText(_translate("MainWindow", "New Item"))
        item = self.list_view.item(10)
        item.setText(_translate("MainWindow", "New Item"))
        item = self.list_view.item(11)
        item.setText(_translate("MainWindow", "New Item"))
        item = self.list_view.item(12)
        item.setText(_translate("MainWindow", "New Item"))
        item = self.list_view.item(13)
        item.setText(_translate("MainWindow", "New Item"))
        self.list_view.setSortingEnabled(__sortingEnabled)
        self.l_videos.setText(_translate("MainWindow", "Видео"))
        self.btn_analyze.setText(_translate("MainWindow", "Распознать людей"))
        self.btn_prev.setText(_translate("MainWindow", "Показать анализ"))
        self.l_appear.setText(_translate("MainWindow", "Время начала видео:"))
        self.input_appear.setDisplayFormat(_translate("MainWindow", "HH:mm:ss"))

    def mySetupUI(self):
        self.list_view.clear()

        self.btn_dir.clicked.connect(self.change_videos_dir)
        self.btn_refresh.clicked.connect(self.update_videos_from_dir)

        self.list_view.currentRowChanged.connect(self.currentRowChanged_handler)
        self.btn_prev.clicked.connect(self.show_analysis)
        self.btn_analyze.clicked.connect(self.start_analyze)

    def analyze_error(self, error):
        logger.critical(error)

    def analyze_finished(self):
        self.list_view.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.SingleSelection)
        self.btn_dir.setEnabled(True)
        self.btn_refresh.setEnabled(True)
        self.btn_analyze.setEnabled(True)
        self.input_appear.setEnabled(True)

        self.video_id, data_path = check_video_db_exists_bypath(self.video_path)
        if self.video_id:
            self.btn_prev.setEnabled(True)
        else:
            self.btn_prev.setEnabled(False)

    def start_analyze(self):
        self.appear_time = self.input_appear.text()
        self.list_view.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.NoSelection)
        self.btn_dir.setEnabled(False)
        self.btn_refresh.setEnabled(False)
        self.btn_analyze.setEnabled(False)
        self.btn_prev.setEnabled(False)
        self.input_appear.setEnabled(False)

        self.thread = QtCore.QThread()
        self.worker = Worker(app_analyze, self.video_path, self.appear_time, self.progress_bar)

        self.worker.moveToThread(self.thread)
        self.worker.signals.error.connect(self.analyze_error)
        self.worker.signals.finished.connect(self.analyze_finished)
        self.worker.signals.finished.connect(self.thread.quit)
        self.worker.signals.finished.connect(self.worker.deleteLater)

        self.thread.started.connect(self.worker.run)
        self.thread.finished.connect(self.thread.deleteLater)

        self.thread.start()

        # self.threadpool.start(worker)

    def show_analysis(self):
        """
        Из app_analysis берется класс и здесь создается. Окно просмотра результатов анализа
        """
        self.form = QtWidgets.QMainWindow()
        self.ui_analyze_window = Ui_analyze()
        self.ui_analyze_window.setupUi(self.form, self.video_id, self.cur_video, self.video_path)
        self.form.show()

    def currentRowChanged_handler(self):
        if self.list_view.currentRow() != -1 and self.list_view.selectionMode() is not QtWidgets.QAbstractItemView.SelectionMode.NoSelection:
            self.cur_video_num = self.list_view.currentRow()
            self.cur_video = self.list_view.currentItem().text()

            self.l_videoname.setText(self.cur_video)
            self.btn_analyze.setEnabled(True)

            self.video_path = os.path.join(self.videos_dir, self.cur_video)
            self.video_id, data_path = check_video_db_exists_bypath(self.video_path)
            if self.video_id:
                self.btn_prev.setEnabled(True)
            else:
                self.btn_prev.setEnabled(False)

            self.cur_video_preview = self.get_preview(self.video_path)
            if self.cur_video_preview:
                pixmap = QtGui.QPixmap(self.cur_video_preview)
                self.l_preview.setPixmap(pixmap)
            else:
                logger.critical('Video preview was not created')

            self.progress_bar.setValue(0)
        else:
            if self.list_view.selectionMode() is not QtWidgets.QAbstractItemView.SelectionMode.NoSelection:
                self.l_preview.clear()
            self.btn_analyze.setEnabled(False)
            self.btn_prev.setEnabled(False)

    def get_preview(self, video_path):
        fixed_width = self.l_preview.width()
        fixed_height = self.l_preview.height()
        new_img = False
        cap = cv.VideoCapture(video_path)
        if cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                logger.critical("Video frame was not read")

            frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
            img = Image.fromarray(frame)
            new_img = img.resize((fixed_width, fixed_height))
            new_img = ImageQt.toqpixmap(new_img).copy()

        else:
            logger.critical("Video Capture is not opened")

        cap.release()
        cv.destroyAllWindows()

        return new_img

    def change_videos_dir(self):
        choose_dir = QtWidgets.QFileDialog.getExistingDirectory(caption='Выберите директорию с видео')
        if os.path.isdir(choose_dir):
            self.videos_dir = choose_dir
            self.update_videos_from_dir()

    def update_videos_from_dir(self):
        if self.videos_dir != '':
            self.list_view.clear()
            self.video_list = []
            self.get_video_list()
            for video in self.video_list:
                item = QtWidgets.QListWidgetItem(self.video_icon, video)
                self.list_view.addItem(item)

    def get_video_list(self):
        for file in os.listdir(self.videos_dir):
            ext = os.path.splitext(self.videos_dir + file)[1]
            if ext != '.mkv' and ext != '.mp4':
                continue
            else:
                self.video_list.append(file)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
