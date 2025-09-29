import sys
import os
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from pathlib import Path
from functools import partial


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))
from exercise17.prob2 import EnhancedCalculator


class CalculatorFileDialog(EnhancedCalculator):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator with File Dialog")

    def _openFile(self):
        home_dir = str(Path.home())
        openFile = QFileDialog.getOpenFileName(self, 'Open file', home_dir)

        if openFile[0]:
            f = open(openFile[0], 'r')
            with f:
                data = f.read()
                self.result_label.setText(data)

            lines = data.splitlines()
            for word in lines:
                num = word.split()
                first_num = num[0]
                sec_num = num[2]
            self.fNum_input.setText(f"{float(first_num):.0f}")
            self.lNum_input.setText(f"{float(sec_num):.0f}")
            

    def _saveFile(self):
        path = os.path.dirname(__file__)
        os.chdir(path)
        fileName = QFileDialog.getSaveFileName(self, 'Save file', str(Path.home()))
        if fileName[0]:
            with open(fileName[0], "w") as file:
                file.write(self.result_label.toPlainText())




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CalculatorFileDialog()
    window.show()
    app.exec()

