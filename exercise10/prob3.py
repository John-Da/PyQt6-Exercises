from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Title Changer")
        self.setFixedSize(QSize(300, 200))

        self.input = QLineEdit()

        self.button = QPushButton("Change Title")
        self.button.clicked.connect(self.click_btn)

        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.button)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

    def click_btn(self):
        title = self.input
        self.setWindowTitle(title.text())


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
