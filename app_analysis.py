# Form implementation generated from reading ui file 'analysis_ui.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
import pandas as pd
from db_processing import select_from_persons
from PIL import Image, ImageQt

class Ui_Form(object):
    def __init__(self):
        self.df_persons = None
        self.video_id = None
        self.cur_img_path = None
        self.cur_img = None

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(975, 479)
        font = QtGui.QFont()
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(239, 239, 239);")
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_show_item = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_show_item.setEnabled(False)
        self.btn_show_item.setGeometry(QtCore.QRect(720, 410, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.btn_show_item.setFont(font)
        self.btn_show_item.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn_show_item.setStyleSheet("QPushButton {\n"
"    border-radius: 20px;\n"
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
        self.btn_show_item.setObjectName("btn_show_item")
        self.l_photobox = QtWidgets.QLabel(parent=self.centralwidget)
        self.l_photobox.setGeometry(QtCore.QRect(66, 60, 200, 400))
        self.l_photobox.setStyleSheet("background-color: rgb(192, 191, 188);")
        self.l_photobox.setText("")
        self.l_photobox.setObjectName("l_photobox")
        self.l_gif = QtWidgets.QLabel(parent=self.centralwidget)
        self.l_gif.setGeometry(QtCore.QRect(400, 60, 200, 400))
        self.l_gif.setStyleSheet("background-color: rgb(192, 191, 188);")
        self.l_gif.setText("")
        self.l_gif.setObjectName("l_gif")
        self.btn_photobox_right = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_photobox_right.setEnabled(False)
        self.btn_photobox_right.setGeometry(QtCore.QRect(270, 230, 31, 51))
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
        self.btn_photobox_left.setGeometry(QtCore.QRect(30, 230, 31, 51))
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
        self.btn_gif_right = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_gif_right.setEnabled(False)
        self.btn_gif_right.setGeometry(QtCore.QRect(610, 230, 31, 51))
        self.btn_gif_right.setStyleSheet("QPushButton {\n"
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
        self.btn_gif_right.setObjectName("btn_gif_right")
        self.btn_gif_left = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_gif_left.setEnabled(False)
        self.btn_gif_left.setGeometry(QtCore.QRect(360, 230, 31, 51))
        self.btn_gif_left.setStyleSheet("QPushButton {\n"
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
        self.btn_gif_left.setObjectName("btn_gif_left")
        self.list_view_items = QtWidgets.QListWidget(parent=self.centralwidget)
        self.list_view_items.setGeometry(QtCore.QRect(700, 60, 241, 331))
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
        self.label_photobox = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_photobox.setGeometry(QtCore.QRect(66, 29, 201, 31))
        self.label_photobox.setStyleSheet("background-color: rgb(255, 120, 0);\n"
"border-color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width: 1px;")
        self.label_photobox.setText("")
        self.label_photobox.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_photobox.setObjectName("label_photobox")
        self.label_gif = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_gif.setGeometry(QtCore.QRect(400, 30, 200, 31))
        self.label_gif.setStyleSheet("background-color: rgb(255, 120, 0);\n"
"border-color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width: 1px;")
        self.label_gif.setText("")
        self.label_gif.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_gif.setObjectName("label_gif")
        self.label_items = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_items.setGeometry(QtCore.QRect(700, 30, 241, 31))
        self.label_items.setStyleSheet("background-color: rgb(255, 120, 0);\n"
"border-color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width: 1px;")
        self.label_items.setText("")
        self.label_items.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_items.setObjectName("label_items")
        self.l_videoname = QtWidgets.QLabel(parent=self.centralwidget)
        self.l_videoname.setGeometry(QtCore.QRect(70, 9, 871, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.l_videoname.setFont(font)
        self.l_videoname.setText("")
        self.l_videoname.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.l_videoname.setObjectName("l_videoname")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.list_view_items.setCurrentRow(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Video analysis of passersby"))
        self.btn_show_item.setText(_translate("MainWindow", "Show item"))
        self.btn_photobox_right.setText(_translate("MainWindow", ">"))
        self.btn_photobox_left.setText(_translate("MainWindow", "<"))
        self.btn_gif_right.setText(_translate("MainWindow", ">"))
        self.btn_gif_left.setText(_translate("MainWindow", "<"))
        self.list_view_items.setSortingEnabled(False)

    def my_setup(self, video_id):
        self.video_id = video_id
        self.df_persons = select_from_persons(self.video_id)
        print(self.df_persons)
        first_person = self.df_persons.iloc[0]
        self.cur_img_path = first_person.photobox
        self.resize_image()
        self.photo_pixmap = QtGui.QPixmap(self.cur_img)
        self.l_photobox.setPixmap(self.photo_pixmap)

    def resize_image(self):
        img = Image.open(self.cur_img_path)
        fixed_width = self.l_photobox.width()
        height_size = self.l_photobox.height()
        new_image = img.resize((fixed_width, height_size))
        self.cur_img = ImageQt.toqpixmap(new_image)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Form()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
