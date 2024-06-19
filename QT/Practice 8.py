# Practice 8 - add to list based on combo-box

import sys
from PyQt5.QtWidgets import QApplication, QDesktopWidget, QMainWindow, QWidget, QListWidget, QComboBox, QPushButton, QVBoxLayout, QHBoxLayout


class MyApp(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setwindow()

        self.list_1 = QListWidget(self)         # define list and place it on the window (self)

        self.combobox_1 = QComboBox(self)       # define combo-box 1
        self.combobox_1.addItems(['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven'])   # add combo-box items

        self.button_1 = QPushButton('Clear', self)  # add clear button

        self.hbox_1 = QHBoxLayout(self)             # define horizontal layout (left to right)
        self.hbox_1.addWidget(self.combobox_1)
        self.hbox_1.addWidget(self.button_1)

        self.vbox_1 = QVBoxLayout(self)             # define vertical layout (top to bottom)
        self.vbox_1.addWidget(self.list_1)
        self.vbox_1.addLayout(self.hbox_1)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)  # place the widget as a whole window

        self.central_widget.setLayout(self.vbox_1)    # set layout to vbox

        self.combobox_1.currentTextChanged.connect(self.combo_change)       # action --> combo-box text to list
        # self.combobox_1.currentIndexChanged.connect(self.combo_change)    # action --> combo-box index to list

        self.button_1.clicked.connect(self.clear)   # action --> clear list

    def combo_change(self, i):
        self.list_1.addItems([str(i)])

    def clear(self):
        self.list_1.clear()

    def setwindow(self):
        self.setWindowTitle("QT-Practice 8")
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
