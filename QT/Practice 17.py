# Practice 17 - Exit button with tool-tip

import sys
from PyQt5.QtWidgets import QApplication, QDesktopWidget, QMainWindow, QWidget, QPushButton, QMessageBox, QToolTip


class MyApp(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setwindow()

        self.button_1 = QPushButton('Exit', self)  # define exit button
        self.button_1.setShortcut('Escape')
        self.button_1.setToolTip('This is exit button, if you want to quit, then quit :)')  # set tool-tip here

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.button_1)  # place the widget as a whole window

        self.button_1.clicked.connect(self.exit)

    def exit(self):
        mbox = QMessageBox.question(self, 'Exit', 'Really want to exit?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if mbox == QMessageBox.Yes:
            self.close()
        elif mbox == QMessageBox.No:
            pass    # do nothing

    def setwindow(self):
        self.setWindowTitle("QT-Practice 17")
        self.setGeometry(0, 0, 200, 100)  # define position and window size

        q_rect = self.frameGeometry()  # window geometry
        cw = QDesktopWidget().availableGeometry().center()  # determine center of the screen loc.
        q_rect.moveCenter(cw)

        self.move(q_rect.topLeft())  # move window to the middle


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.exit(app.exec_())
