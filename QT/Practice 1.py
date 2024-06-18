# Practice 1 - generate window, changing size and position
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget


class MyApp(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setwindow()

    def setwindow(self):
        self.setWindowTitle("QT-Practice 1")
        self.setGeometry(0, 0, 500, 350)    # define position and window size
        # self.resize(500, 350)   # change window size only

        q_rect = self.frameGeometry()   # window geometry
        cw = QDesktopWidget().availableGeometry().center()  # determine center of the screen loc.
        q_rect.moveCenter(cw)
        self.move(q_rect.topLeft())     # move window to the middle


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.exit(app.exec_())
