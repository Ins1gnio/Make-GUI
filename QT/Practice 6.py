# Practice 6 - add to list based on line-edit

import sys
from PyQt5.QtWidgets import QApplication, QDesktopWidget, QMainWindow, QWidget, QListWidget, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout


class MyApp(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setwindow()

        self.list_1 = QListWidget(self)         # define list and place it on the window (self)

        self.lineedit_1 = QLineEdit(self)       # define line-edit

        self.button_1 = QPushButton('Enter', self)  # add enter button
        self.button_1.setShortcut('Return')         # add enter as keyboard shortcut
        self.button_2 = QPushButton('Clear', self)  # add clear button
        self.button_2.setShortcut('Escape')         # add escape as keyboard shortcut

        self.hbox_1 = QHBoxLayout(self)             # define horizontal layout (left to right)
        self.hbox_1.addWidget(self.lineedit_1)
        self.hbox_1.addWidget(self.button_1)
        self.hbox_1.addWidget(self.button_2)

        self.vbox_1 = QVBoxLayout(self)             # define vertical layout (top to bottom)
        self.vbox_1.addWidget(self.list_1)
        self.vbox_1.addLayout(self.hbox_1)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)  # place the widget as a whole window

        self.central_widget.setLayout(self.vbox_1)    # set layout to vbox

        self.button_1.clicked.connect(self.enter)   # action --> enter text to list
        self.button_2.clicked.connect(self.clear)   # action --> clear list

    def enter(self):
        self.list_1.addItems([str(self.lineedit_1.text())])
        self.lineedit_1.clear()

    def clear(self):
        self.list_1.clear()

    def setwindow(self):
        self.setWindowTitle("QT-Practice 6")
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
