import os
import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QApplication


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('design.ui', self)

        self.convert = {
            'seconds': 1,
            'minutes': 60,
            'hours': 3600
        }

        self.reset_button.clicked.connect(self.reset)
        self.ok_button.clicked.connect(self.confirm)

    def reset(self):
        os.system('shutdown -a')
        self.status_text.setText('Tasks deleted')

    def confirm(self):
        current_text = self.choose_time.currentText()
        time = self.time_line.text()
        if not time.isdigit():
            self.status_text.setText('Should be number')
        elif int(time) <= 0:
            self.status_text.setText('Should be more than 0')
        else:
            os.system(f'shutdown -s -t {int(time) * self.convert[current_text]}')
            self.status_text.setText('Task created')


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
