# Practice 15 - LCD display change based on dial

import sys
from PyQt5.QtWidgets import QApplication, QDesktopWidget, QMainWindow, QWidget, QLCDNumber, QDial, QVBoxLayout


class MyApp(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setwindow()

        self.lcd_1 = QLCDNumber(self)   # define lcd

        self.dial_1 = QDial(self)       # define dial
        self.dial_1.setMinimum(0)       # define minimum of dial
        self.dial_1.setMaximum(100)     # define maximum of dial

        self.vbox_1 = QVBoxLayout(self)     # define vertical layout
        self.vbox_1.addWidget(self.lcd_1)
        self.vbox_1.addWidget(self.dial_1)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)      # place the widget as a whole window

        self.central_widget.setLayout(self.vbox_1)      # set layout to vbox

        self.dial_1.sliderMoved.connect(self.slider_change) # action

    def slider_change(self, i):
        self.lcd_1.display(str(i))

    def setwindow(self):
        self.setWindowTitle("QT-Practice 15")
        self.setGeometry(0, 0, 500, 300)    # define position and window size

        q_rect = self.frameGeometry()   # window geometry
        cw = QDesktopWidget().availableGeometry().center()  # determine center of the screen loc.
        q_rect.moveCenter(cw)

        self.move(q_rect.topLeft())     # move window to the middle


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.exit(app.exec_())
