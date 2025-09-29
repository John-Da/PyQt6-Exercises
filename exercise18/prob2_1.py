import sys
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *


class App(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Name Form")
        layout = QVBoxLayout()

        self.button = QPushButton("Click me!")
        self.button.clicked.connect(self.clickBtn)

        self.textLayer = QLabel("Button not clicked yet")

        layout.addWidget(self.button)
        layout.addWidget(self.textLayer)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

    def clickBtn(self):
        self.textLayer.setText("Button was clicked!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = App()
    window.show()
    app.exec()
