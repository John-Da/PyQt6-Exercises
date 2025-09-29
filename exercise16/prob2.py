import sys
import os
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))
from exercise16.prob1 import WindowsMenusToolBar


class ActionConfiguration(WindowsMenusToolBar):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator with Status and Shortcuts")

        self._createShortcuts()
        self.statusbar = self.statusBar()
        self.statusbar.showMessage("Ready")

        self.openAction.setStatusTip("Open a file")
        self.saveAction.setStatusTip("Save a file")
        self.clearAction.setStatusTip("Clear the result")

        self.openAction.triggered.connect(self._openStatus)
        self.saveAction.triggered.connect(self._saveStatus)
        self.exitAction.triggered.connect(self._exitStatus)
        self.clearAction.triggered.connect(self._clearStatus)


        

    def _createShortcuts(self):
        self.openAction.setShortcut(QKeySequence("Ctrl+O"))
        self.saveAction.setShortcut(QKeySequence("Ctrl+S"))
        self.exitAction.setShortcut(QKeySequence("Ctrl+Q"))
        self.clearAction.setShortcut(QKeySequence("Ctrl+R"))

    def _openStatus(self):
        self.statusbar.showMessage("Open a file")

    def _saveStatus(self):
        self.statusbar.showMessage("Save a file")

    def _exitStatus(self):
        self.statusbar.showMessage("Exit the application")

    def _clearStatus(self):
        self.statusbar.showMessage("Clear the result")

    


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ActionConfiguration()
    window.show()
    app.exec()
