# Practice 7 - text size change based on spin-box

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QDesktopWidget, QMainWindow, QWidget, QSpinBox, QLabel, QVBoxLayout, QHBoxLayout


class MyApp(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setwindow()

        self.label_1 = QLabel('PYQT5', self)        # define label 1
        self.label_1.setStyleSheet("font-size: 1px")    # initial font size
        self.label_1.setAlignment(Qt.AlignCenter)  # place text in the middle
        self.label_2 = QLabel('Text Size: ')

        self.spinbox_1 = QSpinBox(self)         # define spin-box then place it in the window (self)
        self.spinbox_1.setMinimum(1)            # set minimum value
        self.spinbox_1.setMaximum(100)          # set maximum value

        self.hbox_1 = QHBoxLayout(self)         # define horizontal layout
        self.hbox_1.addWidget(self.label_2)
        self.hbox_1.addWidget(self.spinbox_1)

        self.vbox_1 = QVBoxLayout(self)         # define vertical layout
        self.vbox_1.addWidget(self.label_1)
        self.vbox_1.addLayout(self.hbox_1)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)      # place the widget as a whole window

        self.central_widget.setLayout(self.vbox_1)      # set layout to vbox

        self.spinbox_1.textChanged.connect(self.spin_change)    # action --> change font size based on spin-box

    def spin_change(self, i):
        style = "font-size: " + str(i) + "px;"
        print(style)
        self.label_1.setStyleSheet(style)  # update font style

    def setwindow(self):
        self.setWindowTitle("QT-Practice 7")
        self.setGeometry(0, 0, 200, 150)    # define position and window size

        q_rect = self.frameGeometry()   # window geometry
        cw = QDesktopWidget().availableGeometry().center()  # determine center of the screen loc.
        q_rect.moveCenter(cw)

        self.move(q_rect.topLeft())     # move window to the middle


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.exit(app.exec_())
