# Practice 18 - How to layout

import sys
from PyQt5.QtWidgets import QApplication, QDesktopWidget, QMainWindow, QWidget, QPushButton, QHBoxLayout, QVBoxLayout


class MyApp(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setwindow()

        self.button_1 = QPushButton('Ok', self)     # define button 1
        self.button_2 = QPushButton('Cancel', self)     # define button 2

        self.hbox_1 = QHBoxLayout(self)     # setting layout 1
        self.hbox_1.addStretch(1)       # add stretch
        self.hbox_1.addWidget(self.button_1)    # setting widget to layout
        self.hbox_1.addWidget(self.button_2)    # setting widget to layout

        self.vbox_1 = QVBoxLayout(self)     # setting layout 2
        self.vbox_1.addStretch(1)       # add stretch
        self.vbox_1.addLayout(self.hbox_1)  # setting layout 1 to 2

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)  # place the widgets in window

        self.central_widget.setLayout(self.vbox_1)

    def setwindow(self):
        self.setWindowTitle("QT-Practice 18")
        self.setGeometry(0, 0, 350, 150)  # define position and window size

        q_rect = self.frameGeometry()  # window geometry
        cw = QDesktopWidget().availableGeometry().center()  # determine center of the screen loc.
        q_rect.moveCenter(cw)

        self.move(q_rect.topLeft())  # move window to the middle


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.exit(app.exec_())
