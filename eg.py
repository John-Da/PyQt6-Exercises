
# print((lambda first, last: f"Fullname: {first} {last}")('Mike','Adam'))

import sys
import os
from PyQt6.QtGui import QMouseEvent
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *


class DrawingBoard(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Drawing Board")

        self.label = QLabel()
        canvas = QPixmap(400, 300)
        canvas.fill(Qt.GlobalColor.white)
        self.label.setPixmap(canvas)


        self.setCentralWidget(self.label)
        
        self.last_x, self.last_y = None, None


    def mouseMoveEvent(self, e):
        if self.last_x is None:
            self.last_x = e.position().x()
            self.last_y = e.position().y()
            return
        
        canvas = self.label.pixmap()
        painter = QPainter(canvas)
        painter.drawLine(self.last_x, self.last_y, e.position().x(), e.position().y())
        painter.end()

        self.label.setPixmap(canvas)

        self.last_x = e.position().x()
        self.last_y = e.position().y()

    
    def mouseReleaseEvent(self, e):
        self.last_x = None
        self.last_y = None
    





if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DrawingBoard()
    window.show()
    app.exec()



