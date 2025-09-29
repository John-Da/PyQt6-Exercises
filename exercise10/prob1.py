from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My First PyQt6 App")
        self.setFixedSize(QSize(300, 200))


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
