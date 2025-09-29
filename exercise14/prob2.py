from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Simple Calculator")
        self.setFixedSize(QSize(400, 500))
        self._createMenuBar()
        self.layouts = QVBoxLayout()

        fNum_layout = QHBoxLayout()
        fNum_layout.addWidget(QLabel("Enter the first number:"))
        self.fNum_input = QLineEdit()
        fNum_layout.addWidget(self.fNum_input)
        self.fNum_input.setMaximumWidth(200)
        self.fNum_input.setStyleSheet("background:yellow; color:#000")
        self.fNum_input.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.layouts.addLayout(fNum_layout)

        lNum_layout = QHBoxLayout()
        lNum_layout.addWidget(QLabel("Enter the second number:"))
        self.lNum_input = QLineEdit()
        self.lNum_input.setMaximumWidth(200)
        lNum_layout.addWidget(self.lNum_input)
        self.lNum_input.setStyleSheet("background:yellow; color:#000")
        self.lNum_input.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.layouts.addLayout(lNum_layout)

        self.btns = ["+", "-", "*", "/", "Clear"]
        self._createBtn()
        self.resultList = []
        self._createResultLayout()

        container = QWidget()
        container.setLayout(self.layouts)

        self.setCentralWidget(container)

    def _createMenuBar(self):
        self.menuBar = self.menuBar()
        self.menuBar.setNativeMenuBar(False)
        self.fileMenu = self.menuBar.addMenu("File")
        self.editMenu = self.menuBar.addMenu("Edit")
        self.configMenu = self.menuBar.addMenu("Config")

    def _createBtn(self):
        btn_layout = QHBoxLayout()
        for btn in self.btns:
            self.operators = QPushButton(btn)
            self.operators.setMaximumWidth(160)
            self.operators.clicked.connect(self.calculate)
            btn_layout.addWidget(self.operators)
        self.layouts.addLayout(btn_layout)

    def _createResultLayout(self):

        result_layout = QHBoxLayout()
        result_layout.addWidget(QLabel("Resutl:"))
        self.result_label = QTextEdit()
        self.result_label.setStyleSheet("background:lightgreen; color:#000")
        result_layout.addWidget(self.result_label)
        self.layouts.addLayout(result_layout)

    def calculate(self):
        inputs = self.sender()
        op = inputs.text()
        try:
            if self.operators == "Clear":
                self.result_label.clear()

            num1 = float(self.fNum_input.text())
            num2 = float(self.lNum_input.text())
            result = eval(f"{num1} {op} {num2}")

            self.resultList.append(f"{num1} {op} {num2} = {result:.2f}")
            self.result_label.setText("\n".join(map(str, self.resultList)))
            # self.clear_inputs()

        except ValueError:
            self.resultList.append("Error: Invalid input")
            self.result_label.setText("\n".join(map(str, self.resultList)))

        except ZeroDivisionError:
            self.resultList.append("Error: Division by zero")
            self.result_label.setText("\n".join(map(str, self.resultList)))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
