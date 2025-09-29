from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from prob3 import NoteApp
import sys


class EnhanceNoteApp(NoteApp):
    def __init__(self):
        super().__init__()

        self.saveBtn.clicked.connect(self.addInputText)
        self.colorDropDown.currentTextChanged.connect(self.changeTextColor)
        self.exitAction.triggered.connect(self.closeApp)

    def addInputText(self):
        self.textInput.append(self.inputInput.text())
        self.inputInput.clear()

    def changeTextColor(self, color):
        self.textInput.setTextColor(QColor(color))

    def clear_inputs(self):
        self.inputInput.clear()

    def closeApp(self):
        app.quit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EnhanceNoteApp()
    window.show()
    app.exec()
