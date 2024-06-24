# Practice 13 - add text to text-edit

import sys
from PyQt5.QtWidgets import QApplication, QDesktopWidget, QMainWindow, QWidget, QTextEdit, QPushButton, QVBoxLayout


class MyApp(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setwindow()

        self.tedit_1 = QTextEdit(self)         # define text edit and place it on the window (self)

        self.button_1 = QPushButton('Clear', self)  # add clear button
        self.button_1.setShortcut('Escape')         # add esc as keyboard shortcut

        self.vbox_1 = QVBoxLayout(self)             # define vertical layout (top to bottom)
        self.vbox_1.addWidget(self.tedit_1)
        self.vbox_1.addWidget(self.button_1)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)  # place the widget as a whole window

        self.central_widget.setLayout(self.vbox_1)    # set layout to vbox

        self.button_1.clicked.connect(self.clear)   # action --> clear list

    def clear(self):
        self.tedit_1.clear()

    def setwindow(self):
        self.setWindowTitle("QT-Practice 13")
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
