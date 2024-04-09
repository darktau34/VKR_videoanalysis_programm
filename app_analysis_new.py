# Form implementation generated from reading ui file 'analysis_ui.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1037, 529)
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
        font.setPointSize(12)
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
"    padding: 8px;\n"
"    padding-left: 0px;\n"
"}\n"
"\n"
"QListView:item{\n"
"    border: 2px solid black;\n"
"    background-color: rgb(192, 191, 188);\n"
"    margin:5px;\n"
"    height:50px;\n"
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
        self.list_view_emotions.setGridSize(QtCore.QSize(120, 60))
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
        font.setWeight(75)
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
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(3)
        self.list_view_items.setCurrentRow(-1)
        self.list_view_emotions.setCurrentRow(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Анализ людей"))
        self.btn_photobox_right.setText(_translate("MainWindow", ">"))
        self.btn_photobox_left.setText(_translate("MainWindow", "<"))
        self.label_appear.setText(_translate("MainWindow", "Время появления: 00:00:00"))
        self.btn_items.setText(_translate("MainWindow", "Распознавание \n"
"предметов"))
        self.btn_emotion.setText(_translate("MainWindow", "Распознавание \n"
"текущей эмоции"))
        self.btn_stats.setText(_translate("MainWindow", "Статистика эмоций\n"
"по всем кадрам"))
        self.btn_video.setText(_translate("MainWindow", "Отрывок видео\n"
"с человеком"))
        self.label_show_item.setText(_translate("MainWindow", "Просмотр предмета"))
        self.list_view_items.setSortingEnabled(False)
        self.label_items.setText(_translate("MainWindow", "Предметы"))
        self.label_facebox.setText(_translate("MainWindow", "Обнаруженное лицо"))
        self.list_view_emotions.setSortingEnabled(False)
        __sortingEnabled = self.list_view_emotions.isSortingEnabled()
        self.list_view_emotions.setSortingEnabled(False)
        item = self.list_view_emotions.item(0)
        item.setText(_translate("MainWindow", "Злость - 69%"))
        item = self.list_view_emotions.item(1)
        item.setText(_translate("MainWindow", "Отвращение - 0%"))
        item = self.list_view_emotions.item(2)
        item.setText(_translate("MainWindow", "Испуг - 8%"))
        item = self.list_view_emotions.item(3)
        item.setText(_translate("MainWindow", "Радость - 34%"))
        item = self.list_view_emotions.item(4)
        item.setText(_translate("MainWindow", "Удивление - 0%"))
        item = self.list_view_emotions.item(5)
        item.setText(_translate("MainWindow", "Нейтрально - 29%"))
        self.list_view_emotions.setSortingEnabled(__sortingEnabled)
        self.label_emotions.setText(_translate("MainWindow", "Распознанные эмоции"))
        self.label_emotionbox.setText(_translate("MainWindow", "Преобладающая эмоция"))
        self.label_emotionname.setText(_translate("MainWindow", "Нейтрально"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
