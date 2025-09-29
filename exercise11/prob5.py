from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Mouse Event Tracking")
        self.setFixedSize(QSize(500, 500))

        self.label = QLabel()
        self.setCentralWidget(self.label)

    def mouseMoveEvent(self, event):
        self.label = QLabel(self) # without self, it shows as new mouse pointer
        self.label.setStyleSheet("background: red")
        self.label.setGeometry(event.pos().x(), event.pos().y(), 10, 10)
        self.label.show()



app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
