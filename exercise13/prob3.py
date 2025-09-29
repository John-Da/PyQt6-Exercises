from PyQt6 import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Color Mixer")
        self.setFixedSize(QSize(300, 200))

        self.userInfo = QLabel()
        self.submit = QPushButton("Submit")
        self.submit.clicked.connect(self.check_input)

        self.info = []

        self.mainlayout = QVBoxLayout()
        self.nameInput = self.create_input("name")
        self.emailInput = self.create_input("email")
        self.ageInput = self.create_input("age")
        self.mainlayout.addWidget(self.submit)
        self.mainlayout.addWidget(self.userInfo)

        container = QWidget()
        container.setLayout(self.mainlayout)
        self.setCentralWidget(container)

    def create_input(self, plname):
        self.inputInfo = QLineEdit()
        self.inputInfo.setMinimumHeight(30)
        self.inputInfo.setPlaceholderText("Enter your " + plname)
        self.mainlayout.addWidget(self.inputInfo)
        self.info.append(self.inputInfo)

    def check_input(self):
        name, email, age = [info.text() for info in self.info]
        if name == "" or email == "" or age == "":
            self.userInfo.setText("Please fill all fields")
        else:
            self.userInfo.setText(f"Name: {name}, Email: {email}, Age: {age}")


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
