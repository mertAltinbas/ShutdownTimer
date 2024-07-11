import sys
from PyQt5.QtGui import QIcon
from PyQt5 import QtWidgets
from shutdownTimerForm import Ui_MainWindow
import os
import time

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('Shutdown Timer')
        self.setWindowIcon(QIcon('timer.png'))

        items = ['Shutdown', 'Restart', 'Sleep', 'Logout', 'Lock']
        self.ui.cbSelecter.addItems(items)

        self.ui.btnStart.clicked.connect(self.start_timer)

    def start_timer(self):
        action = self.ui.cbSelecter.currentText()
        hour_text = self.ui.setHour.text()
        minute_text = self.ui.setMinute.text()
        second_text = self.ui.setSecond.text()

        invlaidInputText = "Invalid input. Please enter numeric values for hour, minute, and second"
        emptyValuesText = "Please fill all values for hour, minute, and second"

        if not hour_text or not minute_text or not second_text:
            QtWidgets.QMessageBox.warning(self, "Attention!", emptyValuesText)
            return

        try:
            hour = int(hour_text)
            minute = int(minute_text)
            second = int(second_text)
        except ValueError:
            QtWidgets.QMessageBox.warning(self, "Attention!", invlaidInputText)
            return

        total_seconds = hour * 3600 + minute * 60 + second

        informationText = f"Starting timer for {action} in {hour} hours, {minute} minutes, and {second} seconds"
        QtWidgets.QMessageBox.information(self, "Information", informationText)

        time.sleep(total_seconds)

        if action == 'Shutdown':
            os.system('shutdown /s /f /t 0')
        elif action == 'Restart':
            os.system('shutdown /r /f /t 0')
        elif action == 'Sleep':
            os.system('rundll32.exe powrprof.dll,SetSuspendState 0,1,0')
        elif action == 'Logout':
            os.system('shutdown /l /f /t 0')
        elif action == 'Lock':
            os.system('rundll32.exe user32.dll,LockWorkStation')

app = QtWidgets.QApplication(sys.argv)
win = Window()
win.show()
sys.exit(app.exec_())