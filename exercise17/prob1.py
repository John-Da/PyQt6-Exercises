import sys
import os
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))
from exercise16.prob2 import ActionConfiguration


class EnhancedCalculator(ActionConfiguration):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator with Actions")

        self.saveAction.triggered.connect(self._saveFile)

        self.openAction.triggered.connect(self._openFile)

        self.clearAction.triggered.connect(self._clearResult)

        self.exitAction.triggered.connect(self._closeApp)

        

    def _closeApp(self):
        app.quit()

    def _clearResult(self):
        self.result_label.clear()
        self.fNum_input.clear()
        self.lNum_input.clear()

    def _saveFile(self):
        path = os.path.dirname(__file__)
        os.chdir(path)
        filename = "result.txt"
        with open(filename, "w") as results:
            results.write(str(self.result_label.toPlainText()))
        self.filePath = os.path.realpath("result.txt")
        self.messages = QMessageBox()
        self.messages.setText(f"Writing result to file {self.filePath}")
        self.messages.exec()

    def _openFile(self):
        path = os.path.dirname(__file__)
        os.chdir(path)
        filename = "result.txt"
        with open(filename, "r") as results:
            resultText = results.read()
            self.result_label.setText(resultText)
        self.filePath = os.path.realpath("result.txt")

        self.messages = QMessageBox()
        self.messages.setText(f"Reading result to file {self.filePath}")
        self.messages.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EnhancedCalculator()
    window.show()
    app.exec()
