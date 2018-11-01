import sys
import time

from astar_nextstation import *

from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *


class StartPage(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, None)
        self.parent = parent
        self.init_start_page()

    def init_start_page(self):
        loader = QUiLoader()
        form = loader.load("UIDesign/start_page.ui")
        self.setCentralWidget(form)
        self.setMinimumSize(1680, 900)

        self.start_button = form.findChild(QPushButton, "startBt")
        self.start_button.clicked.connect(self.changePage)

        self.hour_one_input = form.findChild(QLineEdit, "hrOne")
        self.hour_two_input = form.findChild(QLineEdit, "hrTwo")
        self.min_one_input = form.findChild(QLineEdit, "minOne")
        self.min_two_input = form.findChild(QLineEdit, "minTwo")

        self.hour_one_input.textChanged.connect(self.numberValid)
        self.hour_two_input.textChanged.connect(self.numberValid)
        self.min_one_input.textChanged.connect(self.numberValid)
        self.min_two_input.textChanged.connect(self.numberValid)
        self.updateGUI()

        # attribute
        self.time = []

    def changePage(self):
        if (self.page_time[0] == self.hour_one_input.text() and
                    self.page_time[1] == self.hour_two_input.text() and
                    self.page_time[2] == self.min_one_input.text() and
                    self.page_time[3] == self.min_two_input.text()):
            self.parent.time = "null"

        else:
            day = time.strftime("%a")
            hour = self.hour_one_input.text() + self.hour_two_input.text()
            mins = self.min_one_input.text() + self.min_two_input.text()
            self.parent.time = [day, hour, mins]
        self.parent.changePage(1)

    def numberValid(self, e):
        if e.isdigit():
            if len(e) > 1:
                e = e[1]
            self.sender().setText(e)
        else:
            self.sender().setText("")
        if len(e) == 0:
            self.sender().setText("0")

    def updateGUI(self):

        # update time
        day = time.strftime("%a")
        h, m = time.strftime("%H:%M").split(':')

        self.page_time = [h[0], h[1], m[0], m[1]]
        self.hour_one_input.setText(self.page_time[0])
        self.hour_two_input.setText(self.page_time[1])

        self.min_one_input.setText(self.page_time[2])
        self.min_two_input.setText(self.page_time[3])



'''
def main():
    app = QApplication(sys.argv)

    w = StartPage()
    w.show()
    return app.exec_()


if __name__ == "__main__":
    sys.exit(main())
'''
