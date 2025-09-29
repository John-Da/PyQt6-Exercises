from PyQt6 import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from functools import partial
import sys


class CalculatorApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calulator with slider")

        self.layouts = QVBoxLayout()

        self.sliderOneLabel = QLabel("")
        self.sliderOne = QSlider(Qt.Orientation.Horizontal)
        self.sliderOne.setMaximum(100)
        self.sliderOne.setMinimum(1)
        self.sliderOne.setValue(50)

        self.sliderOne.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.sliderOne.setTickInterval(10)

        self.sliderOneLabel.setText(f"Slider1: {self.sliderOne.value()}")
        self.sliderOne.valueChanged.connect(
            lambda: self.displaynum(self.sliderOneLabel, 1)
        )

        self.layouts.addWidget(self.sliderOneLabel)
        self.layouts.addWidget(self.sliderOne)

        self.sliderTwoLabel = QLabel("")
        self.sliderTwo = QSlider(Qt.Orientation.Horizontal)
        self.sliderTwo.setMaximum(100)
        self.sliderTwo.setMinimum(1)
        self.sliderTwo.setValue(50)

        self.sliderTwo.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.sliderTwo.setTickInterval(10)

        self.sliderTwoLabel.setText(f"Slider2: {self.sliderTwo.value()}")
        self.sliderTwo.valueChanged.connect(
            lambda: self.displaynum(self.sliderTwoLabel, 2)
        )

        self.layouts.addWidget(self.sliderTwoLabel)
        self.layouts.addWidget(self.sliderTwo)

        self.sliders = [self.sliderOne, self.sliderTwo]

        self.btns = ["+", "-", "*", "/", "Clear"]
        self._createBtn()
        self.resultList = []
        self._createResultLayout()

        container = QWidget()
        container.setLayout(self.layouts)

        self.setCentralWidget(container)


    def displaynum(self, numlabel, num):
        numlabel.setText(f"Slider {num}: {self.sender().value()}")

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
            self.operators.clicked.connect(partial(self.calculate, btn))
            btn_layout.addWidget(self.operators)
        self.layouts.addLayout(btn_layout)

    def _createResultLayout(self):

        result_layout = QHBoxLayout()
        self.result_label = QTextEdit()

        result_layout.addWidget(self.result_label)
        self.layouts.addLayout(result_layout)

    def calculate(self, operation):
        g, b = [slider.value() for slider in self.sliders]
        try:
            if operation == "Clear":
                self.result_label.clear()
            else:
                num1 = float(g)
                num2 = float(b)
                result = eval(f"{num1} {operation} {num2}")

                self.resultList.append(f"{num1} {operation} {num2} = {result:.2f}")
                self.result_label.setText("\n".join(map(str, self.resultList)))

        except ValueError:
            self.resultList.append("Error: Invalid input")
            self.result_label.setText("\n".join(map(str, self.resultList)))

        except ZeroDivisionError:
            self.resultList.append("Error: Division by zero")
            self.result_label.setText("\n".join(map(str, self.resultList)))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CalculatorApp()
    window.show()
    app.exec()
