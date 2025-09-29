from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Name Form")
        self.setFixedSize(QSize(400, 500))
        layout = QVBoxLayout()

        fname_layout = QHBoxLayout()
        fname_layout.addWidget(QLabel("First Name:"))
        self.fname_input = QLineEdit()
        fname_layout.addWidget(self.fname_input)
        self.fname_input.setMaximumWidth(200)
        layout.addLayout(fname_layout)

        lname_layout = QHBoxLayout()
        lname_layout.addWidget(QLabel("Last Name:"))
        self.lname_input = QLineEdit()
        self.lname_input.setMaximumWidth(200)
        lname_layout.addWidget(self.lname_input)
        layout.addLayout(lname_layout)

        gender_layout = QHBoxLayout()
        gender_label = QLabel("Gender:")
        self.gender_male = QRadioButton("Male")
        self.gender_female = QRadioButton("Female")
        self.gender_other = QRadioButton("Other")
        gender_layout.addWidget(gender_label)
        gender_layout.addStretch()
        gender_layout.addWidget(self.gender_male)
        gender_layout.addWidget(self.gender_female)
        gender_layout.addWidget(self.gender_other)
        layout.addLayout(gender_layout)

        self.choices = [self.gender_male, self.gender_female, self.gender_other]
        self.inputs = [self.fname_input, self.lname_input]

        btn_layout = QHBoxLayout()
        self.cancel_btn = QPushButton("Cancel")
        self.cancel_btn.clicked.connect(self.clear)
        self.cancel_btn.setStyleSheet("color:red;")

        self.submit_btn = QPushButton("Submit")
        self.submit_btn.setStyleSheet("color:green;")
        self.submit_btn.clicked.connect(self.click_btn)
        btn_layout.addStretch()
        btn_layout.addWidget(self.cancel_btn)
        btn_layout.addWidget(self.submit_btn)
        layout.addLayout(btn_layout)

        result_layout = QHBoxLayout()
        result_layout.addWidget(QLabel("Resutl:"))
        self.result_label = QTextEdit()
        self.result_label.setStyleSheet("background:#fff; color:#000")
        result_layout.addWidget(self.result_label)
        layout.addLayout(result_layout)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

    def click_btn(self):
        fname = self.fname_input.text()
        lname = self.lname_input.text()
        if self.gender_male.isChecked():
            self.result_label.setText(
                f"First Name: {fname}\nLast Name: {lname}\n{self.gender_male.text()} is selected"
            )
        if self.gender_female.isChecked():
            self.result_label.setText(
                f"First Name: {fname}\nLast Name: {lname}\n{self.gender_female.text()} is selected"
            )
        if self.gender_other.isChecked():
            self.result_label.setText(
                f"First Name: {fname}\nLast Name: {lname}\n{self.gender_other.text()} is selected"
            )

    def clear(self):
        for btn in self.choices:
            btn.setAutoExclusive(False)
            btn.setChecked(False)
            btn.setAutoExclusive(True)

        self.fname_input.setText("")
        self.lname_input.setText("")
        self.result_label.setText("")


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
