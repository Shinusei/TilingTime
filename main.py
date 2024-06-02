import sys
import os

import requests

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6 import uic
sudoPassword = '9845'
from PyQt6.QtCore import QTimer, QTime, QDateTime
from bs4 import BeautifulSoup


url = "https://www.google.com/search?q=" + "weather"
html = requests.get(url).content
soup = BeautifulSoup(html, 'html.parser')
temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
str = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text
data = str.split('\n')
sky = data[1].split(',')[0]

class ChangeTime(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(ChangeTime, self).__init__(parent)
        uic.loadUi("D_TilingTimeST.ui", self)
        self.pushButton_2.clicked.connect(self.syncTime)
        self.pushButton.clicked.connect(self.changeTimeZone)

    def syncTime(self):
        os.system('timedatectl set-timezone "$(curl --fail https://ipapi.co/timezone)"')
        p = os.system('echo %s|sudo -S %s' % (sudoPassword, 'systemctl start systemd-timesyncd'))

    def changeTimeZone(self):
        pass


class Date(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Date, self).__init__(parent)
        uic.loadUi("D_TilingTimeC.ui", self)


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
        self.pushButton_2.clicked.connect(self.showCalendar)

        self.pushButton_3.setText(temp + "\n" + sky)
        self.pushButton_3.clicked.connect(self.showWheather)

    def showChangeTime(self):
        self.w = ChangeTime()
        self.w.show()

    def showCalendar(self):
        self.w = Date()
        self.w.show()

    def showWheather(self):
        pass


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
