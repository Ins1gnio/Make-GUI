# Practice 4 - window setting, then add button

import sys
from PyQt5.QtWidgets import QApplication, QDesktopWidget, QPushButton, QMainWindow


class MyApp(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setwindow()

        self.button_1 = QPushButton("Press", self)      # define button, with name and place on the window (self)
        self.button_1.setStyleSheet("background-color: red; font-size: 30px")   # define initial color + font size
        self.button_1.clicked.connect(self.button_1_click)  # signal & slots --> to do action
        self.state = False  # button state

        self.setCentralWidget(self.button_1)    # place the button widget as a whole window

    def button_1_click(self):
        if not self.state:  # state 1
            self.button_1.setStyleSheet("background-color: green; font-size: 30px")
            self.state = True
        else:   # state 2
            self.button_1.setStyleSheet("background-color: red; font-size: 30px")
            self.state = False

    def setwindow(self):
        self.setWindowTitle("QT-Practice 4")
        self.setGeometry(0, 0, 400, 200)    # define position and window size

        q_rect = self.frameGeometry()   # window geometry
        cw = QDesktopWidget().availableGeometry().center()  # determine center of the screen loc.
        q_rect.moveCenter(cw)
        self.move(q_rect.topLeft())     # move window to the middle


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.exit(app.exec_())
