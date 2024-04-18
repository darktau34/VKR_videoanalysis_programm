from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput
from PyQt6.QtMultimediaWidgets import QVideoWidget


class MediaplayerWindow(object):
    def setupUI(self, MainWindow, video_path):
        self.MainWindow = MainWindow
        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.setGeometry(300, 100, 1200, 865)
        self.MainWindow.setFixedWidth(1200)
        self.MainWindow.setFixedHeight(865)
        self.MainWindow.setEnabled(True)
        self.MainWindow.setWindowTitle("Медиапроигрыватель")
        self.MainWindow.setWindowIcon(QtGui.QIcon('player.ico'))

        self.video_path = video_path
        self.media_player = QMediaPlayer(parent=self.MainWindow)
        self.audio = QAudioOutput(parent=self.MainWindow)

        self.video_widget = QVideoWidget(parent=self.MainWindow)
        self.video_widget.setGeometry(10, 10, 1180, 800)
        self.media_player.setVideoOutput(self.video_widget)

        self.btn_play = QtWidgets.QPushButton(parent=self.MainWindow)
        self.btn_play.setGeometry(10, 815, 50, 45)
        self.btn_play.setIcon(self.MainWindow.style().standardIcon(QtWidgets.QStyle.StandardPixmap.SP_MediaPlay))

        self.duration_slider = QtWidgets.QSlider(QtCore.Qt.Orientation.Horizontal, parent=self.MainWindow)
        self.duration_slider.setGeometry(70, 815, 1120, 45)
        self.duration_slider.setRange(0, 0)

        self.media_player.setSource(QtCore.QUrl.fromLocalFile(self.video_path))

        self.media_player.positionChanged.connect(self.mp_position_changed)
        self.media_player.durationChanged.connect(self.mp_duration_changed)
        self.btn_play.clicked.connect(self.video_play_pause)
        self.duration_slider.sliderMoved.connect(self.set_slider_position)

    def video_play_pause(self):
        if self.media_player.isPlaying():
            self.media_player.pause()
            self.btn_play.setIcon(self.MainWindow.style().standardIcon(QtWidgets.QStyle.StandardPixmap.SP_MediaPlay))
        else:
            self.media_player.play()
            self.btn_play.setIcon(self.MainWindow.style().standardIcon(QtWidgets.QStyle.StandardPixmap.SP_MediaPause))

    def mp_position_changed(self, position):
        self.duration_slider.setValue(position)

    def mp_duration_changed(self, duration):
        self.duration_slider.setRange(0, duration)

    def set_slider_position(self, position):
        self.media_player.setPosition(position)


# class MediaplayerWindow(QtWidgets.QWidget):
#     def __init__(self, video_path):
#         super().__init__()
#         self.setGeometry(300, 100, 1200, 860)
#         self.setWindowTitle("Медиапроигрыватель")
#         self.setWindowIcon(QtGui.QIcon('player.ico'))
#
#         self.video_path = video_path
#         self.media_player = QMediaPlayer()
#         self.audio = QAudioOutput()
#
#         self.video_widget = QVideoWidget()
#         self.media_player.setVideoOutput(self.video_widget)
#
#         self.btn_play = QtWidgets.QPushButton()
#         self.btn_play.setIcon(self.style().standardIcon(QtWidgets.QStyle.StandardPixmap.SP_MediaPlay))
#
#         self.duration_slider = QtWidgets.QSlider(QtCore.Qt.Orientation.Horizontal)
#         self.duration_slider.setRange(0, 0)
#
#         hbox = QtWidgets.QHBoxLayout()
#         hbox.addWidget(self.btn_play)
#         hbox.addWidget(self.duration_slider)
#
#         vbox = QtWidgets.QVBoxLayout()
#         vbox.addWidget(self.video_widget)
#         vbox.addLayout(hbox)
#
#         self.setLayout(vbox)
#
#         self.media_player.setSource(QtCore.QUrl.fromLocalFile(self.video_path))
#
#         self.media_player.positionChanged.connect(self.mp_position_changed)
#         self.media_player.durationChanged.connect(self.mp_duration_changed)
#         self.btn_play.clicked.connect(self.video_play_pause)
#         self.duration_slider.sliderMoved.connect(self.set_slider_position)
#
#     def video_play_pause(self):
#         if self.media_player.isPlaying():
#             self.media_player.pause()
#             self.btn_play.setIcon(self.style().standardIcon(QtWidgets.QStyle.StandardPixmap.SP_MediaPlay))
#         else:
#             self.media_player.play()
#             self.btn_play.setIcon(self.style().standardIcon(QtWidgets.QStyle.StandardPixmap.SP_MediaPause))
#
#     def mp_position_changed(self, position):
#         self.duration_slider.setValue(position)
#
#     def mp_duration_changed(self, duration):
#         self.duration_slider.setRange(0, duration)
#
#     def set_slider_position(self, position):
#         self.media_player.setPosition(position)


if __name__ == "__main__":
    import sys
    # app = QtWidgets.QApplication(sys.argv)
    # window = MediaplayerWindow('test.mp4')
    # window.show()
    # sys.exit(app.exec())

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MediaplayerWindow()
    ui.setupUI(MainWindow, 'test/10sec.mp4')
    MainWindow.show()
    sys.exit(app.exec())
