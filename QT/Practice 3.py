# Practice 3 - label text based on window size

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QDesktopWidget, QLabel, QMainWindow


class MyApp(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setwindow()

        self.label_1 = QLabel(self)      # define label and place it on the window (self)
        self.label_1.setStyleSheet("font-size: 30px")   # define font size
        self.label_1.setAlignment(Qt.AlignCenter)   # place text in the middle

        self.setCentralWidget(self.label_1)    # place the label widget as a whole window
        self.label_1.setText('(' + str(self.geometry().height()) + ',' + str(self.geometry().width()) + ')')    # initial text

    def resizeEvent(self, event):
        self.label_1.setText('(' + str(self.geometry().height()) + ',' + str(self.geometry().width()) + ')')    # updated text
        super().resizeEvent(event)  # super class

    def setwindow(self):
        self.setWindowTitle("QT-Practice 3")
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
