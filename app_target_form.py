# Form implementation generated from reading ui file 'target_analysis_ui.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets

from app_target_main import Ui_TargetMain

class Ui_TargetForm(object):
    def __init__(self):
        self.item_index = None
        self.emotion_index = None

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setGeometry(450, 250, 511, 211)
        MainWindow.setFixedWidth(511)
        MainWindow.setFixedHeight(211)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(192, 191, 188))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(192, 191, 188))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(192, 191, 188))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(192, 191, 188))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(192, 191, 188))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(192, 191, 188))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(192, 191, 188))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(192, 191, 188))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(192, 191, 188))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(192, 191, 188))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(192, 191, 188))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(145, 145, 145))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Highlight, brush)
        MainWindow.setPalette(palette)
        MainWindow.setStyleSheet("background-color: rgb(192, 191, 188);")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 251, 151))
        self.frame.setStyleSheet("background-color: rgb(119, 118, 123);\n"
"color: rgb(255, 120, 0);")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.rb_emotions = QtWidgets.QRadioButton(parent=self.frame)
        self.rb_emotions.setGeometry(QtCore.QRect(0, 0, 251, 51))
        self.rb_emotions.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.rb_emotions.setAutoFillBackground(False)
        self.rb_emotions.setStyleSheet("QRadioButton::indicator{\n"
"    width: 32px;\n"
"    height: 32px;\n"
"}\n"
"\n"
"QRadioButton{\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(255, 120, 0);\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: rgb(0, 0, 0);\n"
"    padding-right: 5px;\n"
"}\n"
"")
        self.rb_emotions.setChecked(False)
        self.rb_emotions.setObjectName("rb_emotions")
        self.list_emotions = QtWidgets.QComboBox(parent=self.frame)
        self.list_emotions.setGeometry(QtCore.QRect(10, 70, 231, 41))
        font = QtGui.QFont()
        font.setBold(True)
        self.list_emotions.setFont(font)
        self.list_emotions.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.list_emotions.setPlaceholderText("")
        self.list_emotions.setObjectName("list_emotions")
        self.list_emotions.addItem("")
        self.list_emotions.addItem("")
        self.list_emotions.addItem("")
        self.list_emotions.addItem("")
        self.list_emotions.addItem("")
        self.list_emotions.addItem("")
        self.list_emotions.addItem("")
        self.list_emotions.addItem("")
        self.frame_2 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(260, 0, 251, 151))
        font = QtGui.QFont()
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferDefault)
        self.frame_2.setFont(font)
        self.frame_2.setStyleSheet("background-color: rgb(119, 118, 123);\n"
"color: rgb(255, 120, 0);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.rb_items = QtWidgets.QRadioButton(parent=self.frame_2)
        self.rb_items.setGeometry(QtCore.QRect(0, 0, 251, 51))
        self.rb_items.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.rb_items.setAutoFillBackground(False)
        self.rb_items.setStyleSheet("QRadioButton::indicator{\n"
"    width: 32px;\n"
"    height: 32px;\n"
"}\n"
"\n"
"QRadioButton{\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(255, 120, 0);\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: rgb(0, 0, 0);\n"
"    padding-left: 5px;\n"
"}\n"
"")
        self.rb_items.setChecked(False)
        self.rb_items.setObjectName("rb_items")
        self.list_items = QtWidgets.QComboBox(parent=self.frame_2)
        self.list_items.setGeometry(QtCore.QRect(10, 70, 231, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferDefault)
        self.list_items.setFont(font)
        self.list_items.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.list_items.setPlaceholderText("")
        self.list_items.setObjectName("list_items")
        self.list_items.addItem("")
        self.list_items.addItem("")
        self.list_items.addItem("")
        self.list_items.addItem("")
        self.list_items.addItem("")
        self.list_items.addItem("")
        self.list_items.addItem("")
        self.list_items.addItem("")
        self.list_items.addItem("")
        self.list_items.addItem("")
        self.list_items.addItem("")
        self.list_items.addItem("")
        self.btn_analyze = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_analyze.setEnabled(False)
        self.btn_analyze.setGeometry(QtCore.QRect(0, 150, 511, 61))
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
        font.setBold(False)
        self.btn_analyze.setFont(font)
        self.btn_analyze.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn_analyze.setStyleSheet("QPushButton {\n"
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
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.list_emotions.setCurrentIndex(0)
        self.list_items.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.my_setup_ui()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Таргет-анализ"))
        self.rb_emotions.setText(_translate("MainWindow", "Анализ по эмоциям"))
        self.list_emotions.setCurrentText(_translate("MainWindow", "Злость"))
        self.list_emotions.setItemText(0, _translate("MainWindow", "Злость"))
        self.list_emotions.setItemText(1, _translate("MainWindow", "Грусть"))
        self.list_emotions.setItemText(2, _translate("MainWindow", "Испуг"))
        self.list_emotions.setItemText(3, _translate("MainWindow", "Отвращение"))
        self.list_emotions.setItemText(4, _translate("MainWindow", "Радость"))
        self.list_emotions.setItemText(5, _translate("MainWindow", "Удивление"))
        self.list_emotions.setItemText(6, _translate("MainWindow", "Презрение"))
        self.list_emotions.setItemText(7, _translate("MainWindow", "Нейтрально"))
        self.rb_items.setText(_translate("MainWindow", "Анализ по предметам"))
        self.list_items.setCurrentText(_translate("MainWindow", "Рюкзак"))
        self.list_items.setItemText(0, _translate("MainWindow", "Рюкзак"))
        self.list_items.setItemText(1, _translate("MainWindow", "Зонт"))
        self.list_items.setItemText(2, _translate("MainWindow", "Сумка"))
        self.list_items.setItemText(3, _translate("MainWindow", "Чемодан"))
        self.list_items.setItemText(4, _translate("MainWindow", "Бейсбольная бита"))
        self.list_items.setItemText(5, _translate("MainWindow", "Скейтборд"))
        self.list_items.setItemText(6, _translate("MainWindow", "Бутылка"))
        self.list_items.setItemText(7, _translate("MainWindow", "Нож"))
        self.list_items.setItemText(8, _translate("MainWindow", "Ноутбук"))
        self.list_items.setItemText(9, _translate("MainWindow", "Телефон"))
        self.list_items.setItemText(10, _translate("MainWindow", "Книга"))
        self.list_items.setItemText(11, _translate("MainWindow", "Ножницы"))
        self.btn_analyze.setText(_translate("MainWindow", "Анализировать"))

    def my_setup_ui(self):
        self.rb_emotions.clicked.connect(self.rb_em_clicked)
        self.rb_items.clicked.connect(self.rb_it_clicked)

        self.list_emotions.setEnabled(False)
        self.list_items.setEnabled(False)

        self.btn_analyze.clicked.connect(self.show_analyze)

    def show_analyze(self):
        if self.rb_items.isChecked():
            self.item_index = self.list_items.currentIndex()
            self.emotion_index = None

        if self.rb_emotions.isChecked():
            self.emotion_index = self.list_emotions.currentIndex()
            self.item_index = None

        self.target_main = QtWidgets.QMainWindow()
        self.ui_target_main = Ui_TargetMain(self.item_index, self.emotion_index)
        self.ui_target_main.setupUi(self.target_main)
        self.target_main.show()

    def rb_it_clicked(self):
        self.rb_emotions.setChecked(False)
        if self.rb_items.isChecked():
            self.btn_analyze.setEnabled(True)
            self.list_items.setEnabled(True)
            self.list_emotions.setEnabled(False)
        else:
            self.btn_analyze.setEnabled(False)
            self.list_items.setEnabled(False)

    def rb_em_clicked(self):
        self.rb_items.setChecked(False)
        if self.rb_emotions.isChecked():
            self.btn_analyze.setEnabled(True)
            self.list_emotions.setEnabled(True)
            self.list_items.setEnabled(False)
        else:
            self.btn_analyze.setEnabled(False)
            self.list_emotions.setEnabled(False)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_TargetForm()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
