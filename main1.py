import sys

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QVBoxLayout, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QTimer, QTime, Qt


class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 800, 400)
        layout = QVBoxLayout()
        font = QFont('Arial', 120, QFont.Bold)
        self.label = QLabel()
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(font)
        layout.addWidget(self.label)
        self.setLayout(layout)
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)

    # method called by timer
    def showTime(self):
        current_time = QTime.currentTime()
        label_time = current_time.toString('hh:mm:ss')
        self.label.setText(label_time)


# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# showing all the widgets
window.show()

# start the app
App.exit(App.exec_())
