import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))
from exercise21.prob2 import PaintingBoard

class AnimationWindow(PaintingBoard):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Color of the Day with Animation")
        self._createToolbars()
        self._createMenuBar()
        self._setStatusBar()
        self.animation_action.setStatusTip("Move the label")
        
    def _createMenuBar(self):
        os.chdir(os.path.dirname(__file__))
        self.menutoobar = self.menuBar()
        self.menutoobar.setNativeMenuBar(False)
        self.animation_menu_bar = self.menutoobar.addMenu("Animation")
        
        self.animation_action = QAction(QIcon("move-button.png"), "Move", self)
        self.animation_action.setShortcut(QKeySequence("Ctrl+Shift+M"))
        self.animation_menu_bar.addAction(self.animation_action)
        self.side_toolbar.addAction(self.animation_action)
        
        self.animation_action.triggered.connect(self._update_StatusBar)

        
    def _createToolbars(self):
        self.side_toolbar = QToolBar("Move", self)
        self.addToolBar(Qt.ToolBarArea.TopToolBarArea,self.side_toolbar)
        
        
    def _setStatusBar(self):
        self.statusbar = self.statusBar()
        self.statusbar.showMessage("Ready")
        print(self.label.geometry())
        
        
    def _update_StatusBar(self):
        self.statusbar.showMessage("Move the label")
        self.anim = QPropertyAnimation(self.label, b"geometry")
        self.anim.setDuration(3000)
        # self.anim.setEasingCurve(QEasingCurve.Type.InBounce)
        # self.label.resize(150, 40)
        # self.anim.setEndValue(QPoint(130,20))
        self.anim.setStartValue(QRect(10, 10, 100, 30))
        self.anim.setEndValue(QRect(100, 15, 230, 40))
        self.anim.start()

        
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AnimationWindow()
    window.show()
    app.exec()