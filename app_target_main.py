import logging
import pandas as pd
import cv2 as cv
from PyQt6 import QtCore, QtGui, QtWidgets
from PIL import Image, ImageQt, ImageDraw

from db_processing import select_from_target_table, select_from_persons
from appear_time import EntryTime

logger = logging.getLogger(__name__)

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


class Ui_TargetMain(object):
    def __init__(self, item_index, emotion_index, video_id, video_path):
        self.item_index = item_index
        self.emotion_index = emotion_index
        self.video_id = video_id
        self.video_path = video_path

        self.need_show = True

        self.items_df = None
        self.emotions_df = None
        self.target_df = None
        self.db_persons_df = None

        self.tracker_ids_list = list()
        self.ui_trackers_ids_list = list()

        self.target_type = None

        self.item_dict_translated = {
            0: 'Рюкзак',
            1: 'Зонт',
            2: 'Сумка',
            3: 'Чемодан',
            4: 'Бейсбольная бита',
            5: 'Скейтборд',
            6: 'Бутылка',
            7: 'Нож',
            8: 'Ноутбук',
            9: 'Телефон',
            10: 'Книга',
            11: 'Ножницы'
        }

        self.items_dict = {
            0: 24,
            1: 25,
            2: 26,
            3: 28,
            4: 34,
            5: 36,
            6: 39,
            7: 43,
            8: 63,
            9: 67,
            10: 73,
            11: 76
        }

        self.emotion_dict_translated = {
            0: 'Злость',
            1: 'Грусть',
            2: 'Испуг',
            3: 'Отвращение',
            4: 'Радость',
            5: 'Удивление',
            6: 'Презрение',
            7: 'Нейтрально'
        }

        self.emotions_dict = {
            0: 'angry',
            1: 'sad',
            2: 'fear',
            3: 'disgust',
            4: 'happy',
            5: 'surprise',
            6: 'contempt',
            7: 'neutral'
        }

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(760, 469)
        MainWindow.setFixedWidth(760)
        MainWindow.setFixedHeight(469)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_persons = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_persons.setGeometry(QtCore.QRect(10, 40, 201, 31))
        self.label_persons.setStyleSheet("background-color: rgb(255, 120, 0);\n"
"border-color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width: 2px;")
        self.label_persons.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_persons.setObjectName("label_persons")
        self.list_view_persons = QtWidgets.QListWidget(parent=self.centralwidget)
        self.list_view_persons.setEnabled(True)
        self.list_view_persons.setGeometry(QtCore.QRect(10, 70, 201, 361))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferDefault)
        self.list_view_persons.setFont(font)
        self.list_view_persons.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.list_view_persons.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.list_view_persons.setStyleSheet("QListView{\n"
"    background-color: rgb(119, 118, 123);\n"
"    border-color: rgb(0, 0, 0);\n"
"    border-style: solid;\n"
"    border-width: 2px;\n"
"    padding: 0px;\n"
"    padding-right: 0px;\n"
"    padding-bottom: 0px;\n"
"}\n"
"\n"
"QListView:item{\n"
"    border: 2px solid black;\n"
"    background-color: rgb(192, 191, 188);\n"
"    margin:6px;\n"
"    height:45px;\n"
"    width:160px;\n"
"}\n"
"\n"
"QListView:item:selected{\n"
"    border: 1px solid black;\n"
"    background-color: rgba(255, 120, 0, 171);\n"
"}")
        self.list_view_persons.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.list_view_persons.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.list_view_persons.setAutoScroll(True)
        self.list_view_persons.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.SingleSelection)
        self.list_view_persons.setMovement(QtWidgets.QListView.Movement.Static)
        self.list_view_persons.setFlow(QtWidgets.QListView.Flow.LeftToRight)
        self.list_view_persons.setProperty("isWrapping", True)
        self.list_view_persons.setResizeMode(QtWidgets.QListView.ResizeMode.Fixed)
        self.list_view_persons.setLayoutMode(QtWidgets.QListView.LayoutMode.SinglePass)
        self.list_view_persons.setGridSize(QtCore.QSize(120, 53))
        self.list_view_persons.setViewMode(QtWidgets.QListView.ViewMode.ListMode)
        self.list_view_persons.setModelColumn(0)
        self.list_view_persons.setUniformItemSizes(False)
        self.list_view_persons.setWordWrap(False)
        self.list_view_persons.setSelectionRectVisible(True)
        self.list_view_persons.setObjectName("list_view_persons")
        item = QtWidgets.QListWidgetItem()
        self.list_view_persons.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list_view_persons.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list_view_persons.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list_view_persons.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list_view_persons.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list_view_persons.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list_view_persons.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list_view_persons.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list_view_persons.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list_view_persons.addItem(item)
        self.label_target_type = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_target_type.setGeometry(QtCore.QRect(0, 0, 753, 31))
        self.label_target_type.setStyleSheet("background-color: rgb(255, 120, 0);\n"
"border-color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width: 2px;")
        self.label_target_type.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_target_type.setObjectName("label_target_type")
        self.stackedWidget = QtWidgets.QStackedWidget(parent=self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(210, 39, 541, 421))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_main = QtWidgets.QWidget()
        self.page_main.setObjectName("page_main")
        self.label_time = QtWidgets.QLabel(parent=self.page_main)
        self.label_time.setGeometry(QtCore.QRect(300, 390, 241, 30))
        self.label_time.setStyleSheet("background-color: rgba(0, 0, 0, 0.8);\n"
"color: rgb(255, 120, 0);\n"
"padding-left: 5px;")
        self.label_time.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_time.setObjectName("label_time")
        self.l_photobox = QtWidgets.QLabel(parent=self.page_main)
        self.l_photobox.setGeometry(QtCore.QRect(30, 1, 241, 421))
        self.l_photobox.setStyleSheet("background-color: rgb(192, 191, 188);")
        self.l_photobox.setText("")
        self.l_photobox.setObjectName("l_photobox")
        self.l_item = QtWidgets.QLabel(parent=self.page_main)
        self.l_item.setGeometry(QtCore.QRect(300, 0, 241, 311))
        self.l_item.setStyleSheet("background-color: rgb(192, 191, 188);")
        self.l_item.setText("")
        self.l_item.setObjectName("l_item")
        self.label_counter = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_counter.setGeometry(QtCore.QRect(10, 430, 201, 30))
        self.label_counter.setStyleSheet("background-color: rgba(0, 0, 0, 0.8);\n"
                                      "color: rgb(255, 120, 0);\n"
                                      "padding-left: 5px;\n"
                                      "")
        self.label_counter.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading | QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_counter.setObjectName("label_counter")
        self.label_conf = QtWidgets.QLabel(parent=self.page_main)
        self.label_conf.setGeometry(QtCore.QRect(300, 360, 241, 30))
        self.label_conf.setStyleSheet("background-color: rgba(0, 0, 0, 0.8);\n"
"color: rgb(255, 120, 0);\n"
"padding-left: 5px;\n"
"")
        self.label_conf.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_conf.setObjectName("label_conf")
        self.label_name = QtWidgets.QLabel(parent=self.page_main)
        self.label_name.setGeometry(QtCore.QRect(300, 330, 241, 30))
        self.label_name.setStyleSheet("background-color: rgba(0, 0, 0, 0.8);\n"
"color: rgb(255, 120, 0);\n"
"padding-left: 5px;\n"
"")
        self.label_name.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_name.setObjectName("label_name")
        self.stackedWidget.addWidget(self.page_main)
        self.page_loading = QtWidgets.QWidget()
        self.page_loading.setObjectName("page_loading")
        self.label_loading = QtWidgets.QLabel(parent=self.page_loading)
        self.label_loading.setGeometry(QtCore.QRect(160, 160, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_loading.setFont(font)
        self.label_loading.setStyleSheet("")
        self.label_loading.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_loading.setObjectName("label_loading")
        self.l_loading = QtWidgets.QLabel(parent=self.page_loading)
        self.l_loading.setGeometry(QtCore.QRect(120, 200, 301, 41))
        self.l_loading.setStyleSheet("")
        self.l_loading.setText("")
        self.l_loading.setObjectName("l_loading")
        self.stackedWidget.addWidget(self.page_loading)
        self.stackedWidget.raise_()
        self.label_persons.raise_()
        self.list_view_persons.raise_()
        self.label_target_type.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.list_view_persons.setCurrentRow(-1)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.my_setup_ui()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Таргет-анализ"))
        self.label_persons.setText(_translate("MainWindow", "Список людей"))
        self.list_view_persons.setSortingEnabled(False)
        __sortingEnabled = self.list_view_persons.isSortingEnabled()
        self.list_view_persons.setSortingEnabled(False)
        item = self.list_view_persons.item(0)
        item.setText(_translate("MainWindow", "Человек 1"))
        item = self.list_view_persons.item(1)
        item.setText(_translate("MainWindow", "Человек 2"))
        item = self.list_view_persons.item(2)
        item.setText(_translate("MainWindow", "Человек 3"))
        item = self.list_view_persons.item(3)
        item.setText(_translate("MainWindow", "Человек 4"))
        item = self.list_view_persons.item(4)
        item.setText(_translate("MainWindow", "Человек 5"))
        item = self.list_view_persons.item(5)
        item.setText(_translate("MainWindow", "Человек 6"))
        item = self.list_view_persons.item(6)
        item.setText(_translate("MainWindow", "Человек 7"))
        item = self.list_view_persons.item(7)
        item.setText(_translate("MainWindow", "Человек 8"))
        item = self.list_view_persons.item(8)
        item.setText(_translate("MainWindow", "Человек 9"))
        item = self.list_view_persons.item(9)
        item.setText(_translate("MainWindow", "Человек 10"))
        self.list_view_persons.setSortingEnabled(__sortingEnabled)
        self.label_target_type.setText(_translate("MainWindow", "Таргет-анализ эмоций: Злость"))
        self.label_time.setText(_translate("MainWindow", "Время обнаружения: 00:00:00"))
        self.label_conf.setText(_translate("MainWindow", "Уверенность модели: 59%"))
        self.label_name.setText(_translate("MainWindow", "Эмоция: Злость"))
        self.label_loading.setText(_translate("MainWindow", "Загрузка"))

    def my_setup_ui(self):
        if self.emotion_index is not None:
            self.target_type = True
        else:
            self.target_type = False

        if self.target_type:
            self.label_target_type.setText(f'Таргет анализ эмоций: {self.emotion_dict_translated.get(self.emotion_index)}')
        else:
            self.label_target_type.setText(f'Таргет анализ предметов: {self.item_dict_translated.get(self.item_index)}')

        self.list_view_persons.clear()
        self.label_name.clear()
        self.label_conf.clear()
        self.label_time.clear()

        items_df_path, emotions_df_path = select_from_target_table(self.video_id)
        self.items_df = pd.read_csv(items_df_path)
        self.emotions_df = pd.read_csv(emotions_df_path)

        if self.target_type:
            self.target_df = self.emotions_df.loc[self.emotions_df.emotion == self.emotions_dict.get(self.emotion_index)]
        else:
            self.target_df = self.items_df.loc[self.items_df.item_id == self.items_dict.get(self.item_index)]

        if self.target_df.empty:
            self.need_show = False
            dlg = DialogWindowMessage('Внимание',
                                      'Люди не найдены')
            dlg.exec()

        for i in self.target_df.tracker_id.unique():
            self.tracker_ids_list.append(int(i))

        self.tracker_ids_list.sort()

        self.label_counter.setText(f'Количество людей: {len(self.tracker_ids_list)}')

        self.db_persons_df = select_from_persons(self.video_id)

        for i in self.tracker_ids_list:
            ui_tracker = self.db_persons_df[self.db_persons_df.tracker_id == i].ui_tracker_id.values[0]
            self.ui_trackers_ids_list.append(ui_tracker)
            item = QtWidgets.QListWidgetItem(f'Человек {ui_tracker}')
            self.list_view_persons.addItem(item)

        self.list_view_persons.currentRowChanged.connect(self.persons_currentRowChanged_handler)
        self.list_view_persons.setCurrentRow(0)

    def persons_currentRowChanged_handler(self):
        cur_row_id = self.list_view_persons.currentRow()
        tracker_id = self.tracker_ids_list[cur_row_id]

        target_tracker_df = self.target_df.loc[self.target_df.tracker_id == tracker_id]
        target_tracker_df.reset_index(drop=True, inplace=True)
        max_conf_id = target_tracker_df.conf.idxmax()
        max_conf_row = target_tracker_df.iloc[max_conf_id]

        frame_number = int(max_conf_row.frame)
        box_ph_str = max_conf_row.xyxy_ph
        box_it_str = max_conf_row.xyxy
        box_ph = self.parse_tuple(box_ph_str)
        box_it = self.parse_tuple(box_it_str)

        frame, video_fps = self.get_video_frame(frame_number)
        if frame is None:
            logger.error('Video frame is None')

        pil_im = Image.fromarray(frame)

        self.add_person_photobox(pil_im, box_ph, box_it)
        self.add_item_photobox(pil_im, box_ph, box_it)

        conf = round(max_conf_row.conf * 100)
        entry_time = EntryTime('00:00:00', None, None, None)
        detection_time = entry_time.get_solo_entry_time(frame_number, video_fps)

        if self.target_type:
            self.label_name.setText(f'Эмоция: {self.emotion_dict_translated.get(self.emotion_index)}')
        else:
            self.label_name.setText(f'Предмет: {self.item_dict_translated.get(self.item_index)}')

        self.label_conf.setText(f'Уверенность модели: {conf}%')
        self.label_time.setText(f'Время обнаружения: {detection_time}')


    def get_video_frame(self, frame_number):
        cap = cv.VideoCapture(self.video_path)
        fps = int(cap.get(cv.CAP_PROP_FPS))

        frame_target = None

        if cap.isOpened():
            cap.set(cv.CAP_PROP_POS_FRAMES, frame_number)
            ret, frame_target = cap.read()
            if not ret:
                logger.error('Not Ret')
        else:
            logger.error("Video Capture is not opened")

        cap.release()
        frame_target = cv.cvtColor(frame_target, cv.COLOR_BGR2RGB)
        return frame_target, fps

    def parse_tuple(self, box_str_tuple):
        box_str_tuple = box_str_tuple[1:-1]
        box_elements = box_str_tuple.split(', ')
        box_tuple = (int(box_elements[0]), int(box_elements[1]), int(box_elements[2]), int(box_elements[3]))
        return box_tuple

    def add_item_photobox(self, pil_img, box_ph, box_it):
        photobox = pil_img.crop(box_ph)
        itembox = photobox.crop(box_it)
        itembox = self.resize_image(itembox, self.l_item)
        cur_itembox_pixmap = QtGui.QPixmap(itembox)
        self.l_item.setPixmap(cur_itembox_pixmap)

    def add_person_photobox(self, pil_img, box_ph, box_it):
        photobox = pil_img.crop(box_ph)

        draw = ImageDraw.Draw(photobox)
        draw.rectangle(box_it, outline=(0, 255, 0), width=1)

        photobox = self.resize_image(photobox, self.l_photobox)
        cur_photobox_pixmap = QtGui.QPixmap(photobox)
        self.l_photobox.setPixmap(cur_photobox_pixmap)

    def resize_image(self, img, l_imgbox):
        fixed_width = l_imgbox.width()
        fixed_height = l_imgbox.height()
        new_image = img.resize((fixed_width, fixed_height))
        new_img = ImageQt.toqpixmap(new_image).copy()
        return new_img

    def resize_image_bypath(self, img_path, l_imgbox):
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
    ui = Ui_TargetMain(0, None)
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
