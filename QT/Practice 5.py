# Practice 5 - simple id password input

import sys
from PyQt5.QtWidgets import QApplication, QDesktopWidget, QMainWindow, QWidget, QLabel, QLineEdit, QPushButton, QGridLayout


class MyApp(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setwindow()

        self.label_1 = QLabel('ID', self)           # define label for id
        self.label_2 = QLabel('Password', self)     # define label for password

        self.lineedit_1 = QLineEdit(self)           # define lineedit for id
        self.lineedit_2 = QLineEdit(self)           # define lineedit for password

        self.button_1 = QPushButton('Enter', self)      # button enter
        self.button_2 = QPushButton('Cancel', self)     # button cancel

        self.glayout = QGridLayout(self)    # set grid layout (0, 0 is top left)

        self.glayout.addWidget(self.label_1, 0, 0)
        self.glayout.addWidget(self.label_2, 1, 0)

        self.glayout.addWidget(self.lineedit_1, 0, 1, 1, 2)
        self.glayout.addWidget(self.lineedit_2, 1, 1, 1, 2)

        self.glayout.addWidget(self.button_1, 2, 1)
        self.glayout.addWidget(self.button_2, 2, 2)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)  # place the widget as a whole window

        self.central_widget.setLayout(self.glayout)    # set layout to glayout

    def setwindow(self):
        self.setWindowTitle("QT-Practice 5")
        self.setGeometry(0, 0, 200, 100)    # define position and window size

        q_rect = self.frameGeometry()   # window geometry
        cw = QDesktopWidget().availableGeometry().center()  # determine center of the screen loc.
        q_rect.moveCenter(cw)

        self.move(q_rect.topLeft())     # move window to the middle


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.exit(app.exec_())
