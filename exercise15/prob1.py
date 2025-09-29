from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Menu Example")
        self.setFixedSize(QSize(400, 500))
        self._createMenuBar()
        self._addMenus()

    def _createMenuBar(self):
        self.menuBar = self.menuBar()
        self.menuBar.setNativeMenuBar(False)
        self.fileMenu = self.menuBar.addMenu("File")
        self.editMenu = self.menuBar.addMenu("Edit")
        self.helpMenu = self.menuBar.addMenu("Help")

    def _createFileTB(self):
        self.newToolBar = self.addToolBar("New")
        self.openToolBar = self.addToolBar("Open")
        self.saveToolBar = self.addToolBar("Save")
        self.exitToolBar = self.addToolBar("Exit")

    def _addMenus(self):
        self._addFileMenu()
        self._addEditMenu()
        self._addHelpMenu()

    def _addFileMenu(self):
        self.newAction = QAction("New", self)
        self.openAction = QAction("Open", self)
        self.saveAction = QAction("Save", self)
        self.exitAction = QAction("Exit", self)
        self.fileMenu.addAction(self.newAction)
        self.fileMenu.addAction(self.openAction)
        self.fileMenu.addAction(self.saveAction)
        self.fileMenu.addAction(self.exitAction)

    def _addEditMenu(self):
        self.cutAction = QAction("Cut", self)
        self.copyAction = QAction("Copy", self)
        self.pasteAction = QAction("Paste", self)
        self.editMenu.addAction(self.cutAction)
        self.editMenu.addAction(self.copyAction)
        self.editMenu.addAction(self.pasteAction)

    def _addHelpMenu(self):
        self.helpAction = QAction("About", self)
        self.helpMenu.addAction(self.helpAction)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
