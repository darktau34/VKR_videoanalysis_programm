from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

import sys


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle('First Qt GUI')
        self.setGeometry(300, 200, 400, 500)

        self.counter = 0

        self.text1 = QtWidgets.QLabel(self)
        self.text1.setText(f'Counter is {self.counter}')
        self.text1.move(100, 100)
        self.text1.adjustSize()

        self.btn = QtWidgets.QPushButton(self)
        self.btn.move(50, 50)
        self.btn.setText('Click me')
        self.btn.setFixedWidth(100)
        self.btn.clicked.connect(self.btn_handler)



    def btn_handler(self):
        self.counter += 1
        self.text1.setText(f'Counter is {self.counter}')
        self.text1.adjustSize()

def application():
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    application()
