from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Toolbar Example")
        self.setFixedSize(QSize(400, 500))

        self._creatToolBar()
        self._createTBMenu()

    def _creatToolBar(self):
        self.sideToolBar = QToolBar("Help", self)
        self.addToolBar(Qt.ToolBarArea.LeftToolBarArea, self.sideToolBar)

    def _createTBMenu(self):
        self.cutAction = QAction("Cut", self)
        self.copyAction = QAction("Copy", self)
        self.pasteAction = QAction("Paste", self)
        self.sideToolBar.addAction(self.cutAction)
        self.sideToolBar.addAction(self.copyAction)
        self.sideToolBar.addAction(self.pasteAction)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
