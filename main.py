import sys

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6 import uic
from PyQt6.QtCore import QTimer, QTime, QDateTime
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QTimeEdit, QWidget, QVBoxLayout, QLabel


class ChangeTime(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(ChangeTime, self).__init__(parent)
        uic.loadUi("D_TilingTimeST.ui", self)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("D_TilingTimeM.ui", self)
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(100)

    def showTime(self):
        current_time = QDateTime.currentDateTime()
        label_time = current_time.toString('''hh:mm:ss'\n'dd.MM.yyyy''')
        self.timeEdit.setText(label_time)
        self.pushButton.clicked.connect(self.showChangeTime)

    def showChangeTime(self):
        self.w = ChangeTime()
        self.w.show()


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
