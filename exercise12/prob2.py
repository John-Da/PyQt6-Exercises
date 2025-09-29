from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Name Form")
        self.setFixedSize(QSize(400, 200))

        self.label1 = QLabel("First Name:")
        font = self.label1.font()
        font.setPointSize(20)
        self.label1.setFont(font)

        self.label2 = QLabel("Last Name:")
        font = self.label2.font()
        font.setPointSize(20)
        self.label2.setFont(font)

        self.input1 = QLineEdit()
        font = self.input1.font()
        font.setPointSize(20)
        self.input1.setFont(font)

        self.input2 = QLineEdit()
        font = self.input2.font()
        font.setPointSize(20)
        self.input2.setFont(font)

        self.cancel = QPushButton("Cancel")
        self.cancel.setMaximumWidth(120)
        font = self.cancel.font()
        font.setPointSize(20)
        self.cancel.setFont(font)
        self.cancel.setStyleSheet("color:red;")

        self.submit = QPushButton("Submit")
        self.submit.setMaximumWidth(120)
        font = self.submit.font()
        font.setPointSize(20)
        self.submit.setFont(font)
        self.submit.setStyleSheet("color:green;")

        vlayout = QHBoxLayout()
        vlayout.addWidget(self.label1)
        vlayout.addWidget(self.input1)
        vlayout.setSpacing(80)

        slayout = QHBoxLayout()
        slayout.addWidget(self.label2)
        slayout.addWidget(self.input2)
        slayout.setSpacing(80)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.cancel)
        button_layout.addWidget(self.submit)
        button_layout.setSpacing(20)

        overall = QVBoxLayout()
        overall.addLayout(vlayout)
        overall.addLayout(slayout)
        overall.addLayout(button_layout)

        container = QWidget()
        container.setLayout(overall)

        self.setCentralWidget(container)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
