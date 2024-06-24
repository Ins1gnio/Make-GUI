# Practice 14 - progress bar

import sys, time
from PyQt5.QtWidgets import QApplication, QDesktopWidget, QMainWindow, QWidget, QProgressBar, QPushButton, QGridLayout


class MyApp(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setwindow()

        self.pb_1 = QProgressBar(self)         # define progress bar and place it on the window (self)

        self.button_1 = QPushButton('Start-1', self)  # add start-1 button
        self.button_2 = QPushButton('Start-2', self)  # add start-2 button

        self.glayout_1 = QGridLayout(self)      # set grid layout (0, 0 is top left)
        self.glayout_1.addWidget(self.button_1, 0, 0)
        self.glayout_1.addWidget(self.button_2, 0, 1)
        self.glayout_1.addWidget(self.pb_1, 1, 0, 1, 3)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)  # place the widget as a whole window

        self.central_widget.setLayout(self.glayout_1)    # set layout to grid layout

        self.button_1.clicked.connect(self.start_1)
        self.button_2.clicked.connect(self.start_2)

    def start_1(self):
        for i in range(101):    # 0 to 100 %
            time.sleep(0.01)
            self.pb_1.setValue(i)

    def start_2(self):
        slices = 8
        for i in range(slices):
            for j in range(int(i * 100 / slices), int((i + 1) * 100 / slices) + 1):    # 0 to 100 %
                time.sleep(0.01)
                self.pb_1.setValue(j)
            time.sleep(0.2)


    def setwindow(self):
        self.setWindowTitle("QT-Practice 14")
        self.setGeometry(0, 0, 400, 100)    # define position and window size

        q_rect = self.frameGeometry()   # window geometry
        cw = QDesktopWidget().availableGeometry().center()  # determine center of the screen loc.
        q_rect.moveCenter(cw)

        self.move(q_rect.topLeft())     # move window to the middle


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.exit(app.exec_())
