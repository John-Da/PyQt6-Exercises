import sys
import os
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))
from exercise17.prob2 import MessageBoxDisplay


class RobustCalculator(MessageBoxDisplay):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Robust Calculator")

        self.openAction.triggered.connect(self._openFileaa) 

    def _openFileaa(self):
        path = os.path.dirname(__file__)
        os.chdir(path)
        filename = "result.txt"
        self.filePath = os.path.realpath("result.txt")

        self.inputList = []

        try:
            with open(filename, "r") as results:
                resultText = results.read()
                self.result_label.setText(resultText)

                lines = resultText.splitlines()
                for word in lines:
                    num = word.split()
                    first_num = num[0]
                    sec_num = num[2]
                self.fNum_input.setText(f"{float(first_num):.0f}")
                self.lNum_input.setText(f"{float(sec_num):.0f}")

        except FileNotFoundError:
            self.messages = QMessageBox()
            self.messages.setText(f"File not found. Please save a file first.")
            self.messages.exec()
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RobustCalculator()
    window.show()
    app.exec()
