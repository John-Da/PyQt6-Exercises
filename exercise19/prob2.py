import sys
import os
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *



sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))
from exercise19.prob1 import CalculatorFileDialog


class CalculorDialogs(CalculatorFileDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculator Dialogs")
        self.colorAction.triggered.connect(self.changecolor)
        self.sizeAction.triggered.connect(self.changefont)


    def changecolor(self):
        col = QColorDialog.getColor()
        if col.isValid():
            self.result_label.setStyleSheet(f"background-color:{col.name()}")

    def changefont(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.result_label.setfont(font)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CalculorDialogs()
    window.show()
    app.exec()
