# Practice 1 - Generate window, changing size and position
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setwindow()

    def setwindow(self):
        self.setWindowTitle("QT-Practice 1")
        self.setGeometry(0, 0, 500, 350)    # define position and window size
        # self.resize(500, 350)   # change window size only

        # re-position window in the middle
        q_rect = self.frameGeometry()   # window geometry
        cw = QDesktopWidget().availableGeometry().center()  # determine center of the screen loc.
        q_rect.moveCenter(cw)
        self.move(q_rect.topLeft())

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
