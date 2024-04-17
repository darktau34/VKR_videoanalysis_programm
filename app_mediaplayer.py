from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput
from PyQt6.QtMultimediaWidgets import QVideoWidget


class MediaplayerWindow(QtWidgets.QWidget):
    def __init__(self, video_path):
        super().__init__()
        self.setGeometry(300, 100, 1200, 860)
        self.setWindowTitle("Медиапроигрыватель")
        self.setWindowIcon(QtGui.QIcon('player.ico'))

        self.video_path = video_path
        self.media_player = QMediaPlayer()
        self.audio = QAudioOutput()

        self.video_widget = QVideoWidget()
        self.media_player.setVideoOutput(self.video_widget)

        self.btn_play = QtWidgets.QPushButton()
        self.btn_play.setIcon(self.style().standardIcon(QtWidgets.QStyle.StandardPixmap.SP_MediaPlay))

        self.duration_slider = QtWidgets.QSlider(QtCore.Qt.Orientation.Horizontal)
        self.duration_slider.setRange(0, 0)

        hbox = QtWidgets.QHBoxLayout()
        hbox.addWidget(self.btn_play)
        hbox.addWidget(self.duration_slider)

        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(self.video_widget)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.media_player.setSource(QtCore.QUrl.fromLocalFile(self.video_path))

        self.media_player.positionChanged.connect(self.mp_position_changed)
        self.media_player.durationChanged.connect(self.mp_duration_changed)
        self.btn_play.clicked.connect(self.video_play_pause)
        self.duration_slider.sliderMoved.connect(self.set_slider_position)

    def video_play_pause(self):
        if self.media_player.isPlaying():
            self.media_player.pause()
            self.btn_play.setIcon(self.style().standardIcon(QtWidgets.QStyle.StandardPixmap.SP_MediaPlay))
        else:
            self.media_player.play()
            self.btn_play.setIcon(self.style().standardIcon(QtWidgets.QStyle.StandardPixmap.SP_MediaPause))

    def mp_position_changed(self, position):
        self.duration_slider.setValue(position)

    def mp_duration_changed(self, duration):
        self.duration_slider.setRange(0, duration)

    def set_slider_position(self, position):
        self.media_player.setPosition(position)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MediaplayerWindow('test.mp4')
    window.show()
    sys.exit(app.exec())
