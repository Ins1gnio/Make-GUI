# Practice 10 - double spin-box

import sys
from PyQt5.QtWidgets import QApplication, QDesktopWidget, QMainWindow, QDoubleSpinBox


class MyApp(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setwindow()

        self.dspinbox_1 = QDoubleSpinBox(self)      # define double spin-box then place it in the window (self)
        self.dspinbox_1.setMinimum(-10)             # set minimum value
        self.dspinbox_1.setMaximum(10)              # set maximum value
        self.dspinbox_1.setSingleStep(0.01)         # set one step (one click)

        self.setCentralWidget(self.dspinbox_1)      # place the widget as a whole window

    def setwindow(self):
        self.setWindowTitle("QT-Practice 10")
        self.setGeometry(0, 0, 100, 50)    # define position and window size

        q_rect = self.frameGeometry()   # window geometry
        cw = QDesktopWidget().availableGeometry().center()  # determine center of the screen loc.
        q_rect.moveCenter(cw)

        self.move(q_rect.topLeft())     # move window to the middle


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.exit(app.exec_())
