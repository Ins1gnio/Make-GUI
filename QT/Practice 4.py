# Practice 4 - generate window, label, and check box, then modify text based on check box's state
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QDesktopWidget, QMainWindow, QWidget, QLabel, QCheckBox, QVBoxLayout


class MyApp(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setwindow()

        self.label_1 = QLabel('PYQT5', self)      # define label and place it on the window (self)
        self.label_1.setStyleSheet("font-size: 30px")   # define font size
        self.label_1.setAlignment(Qt.AlignCenter)   # place text in the middle

        self.checkbox_1 = QCheckBox("Bold?", self)  # check-box 1 for bold
        self.checkbox_2 = QCheckBox("Italic?", self)    # check-box 2 for italic
        self.checkbox_3 = QCheckBox("Underline?", self)     # check-box 3 for underline

        self.vbox = QVBoxLayout(self)           # define vertical layout (top to bottom)
        self.vbox.addWidget(self.label_1)
        self.vbox.addWidget(self.checkbox_1)
        self.vbox.addWidget(self.checkbox_2)
        self.vbox.addWidget(self.checkbox_3)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)  # place the widget as a whole window

        self.central_widget.setLayout(self.vbox)    # set layout to vbox

        self.checkbox_1.clicked.connect(self.update_style)  # action 1
        self.checkbox_2.clicked.connect(self.update_style)  # action 2
        self.checkbox_3.clicked.connect(self.update_style)  # action 3

    def update_style(self):
        style = "font-size: 30px;"  # default font style

        if self.checkbox_1.isChecked():
            style += " font-weight: bold;"
        if self.checkbox_2.isChecked():
            style += " font-style: italic;"
        if self.checkbox_3.isChecked():
            style += " text-decoration: underline;"

        print(style)
        self.label_1.setStyleSheet(style)   # update font style

    def setwindow(self):
        self.setWindowTitle("QT-Practice 4")
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
