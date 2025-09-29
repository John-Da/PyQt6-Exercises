import sys
import os
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *


class DrawingBoard(QMainWindow):
    def __init__(self):
        super().__init__()

        self.SCREEN_WIDTH = 400
        self.SCREEN_HIGHT = 400

        self.label = QLabel()
        canvas = QPixmap(self.SCREEN_WIDTH, self.SCREEN_HIGHT)
        canvas.fill(Qt.GlobalColor.white)
        self.label.setPixmap(canvas)

        self.setCentralWidget(self.label)
        self.draw_shapes()

    def draw_shapes(self):
        canvas = self.label.pixmap()
        painter = QPainter(canvas)
        pen = QPen()
        pen.setWidth(3)
        pen.setColor(QColor("green"))
        painter.setPen(pen)

        pen.setStyle(Qt.PenStyle.DashDotDotLine)
        painter.setPen(pen)
        painter.drawRect(
            (self.SCREEN_WIDTH // 2) - (300 // 2),
            (self.SCREEN_HIGHT // 2) - (300 // 2),
            300, 300,
        )

        pen.setColor(QColor("blue"))
        pen.setWidth(1)
        pen.setStyle(Qt.PenStyle.SolidLine)
        painter.setPen(pen)

        brush = QBrush()
        brush.setColor(QColor("black"))
        brush.setStyle(Qt.BrushStyle.Dense7Pattern)
        painter.setBrush(brush)
        painter.drawEllipse(
            (int(canvas.width()) // 2) - (300 // 2) + 50,
            (int(canvas.height()) // 2) - (300 // 2) + 50,
            200, 200,
        )

        pen.setColor(QColor("red"))
        painter.setFont(QFont('default', 24))
        painter.setPen(pen)
        painter.drawText(
            100, 100, 200, 200,
            Qt.AlignmentFlag.AlignCenter,
            "Yen Da Hwa",
        )

        painter.end()
        self.label.setPixmap(canvas)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DrawingBoard()
    window.show()
    app.exec()
