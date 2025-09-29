import sys
import os
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from functools import partial


class PaintingBoard(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Color of the Day")

        self.SCREEN_WIDTH = 400
        self.SCREEN_HIGHT = 400

        self.layouts = QVBoxLayout()

        self.label = QLabel()
        self.label.setFont(QFont("default", 40))

        self.canvas_label = QLabel()
        canvas = QPixmap(self.SCREEN_WIDTH, self.SCREEN_HIGHT)
        canvas.fill(Qt.GlobalColor.white)
        self.canvas_label.setPixmap(canvas)

        self.btns = [
            "#FF0000",
            "#FFFF00",
            "#FFC0CB",
            "#008000",
            "#FFA500",
            "#0000FF",
            "#800080",
        ]

        self.days = {
            "#FF0000": "Sunday",
            "#FFFF00": "Monday",
            "#FFC0CB": "Tuesday",
            "#008000": "Wednesday",
            "#FFA500": "Thursday",
            "#0000FF": "Friday",
            "#800080": "Saturday",
        }

        self.layouts.addWidget(self.label)
        self.layouts.addWidget(self.canvas_label)
        self._createBtn()

        container = QWidget()
        container.setLayout(self.layouts)
        self.setCentralWidget(container)

    def _createBtn(self):
        btn_layout = QHBoxLayout()
        for btn in self.btns:
            self.colorBtn = QPushButton()
            self.colorBtn.setMaximumWidth(24)
            self.colorBtn.setStyleSheet(f"background:{btn}")
            self.colorBtn.clicked.connect(partial(self.update_day, btn))
            btn_layout.addWidget(self.colorBtn)
        self.layouts.addLayout(btn_layout)

    def update_day(self, c):
        day = self.days[c]
        self.label.setText(day)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.draw_shapes(c)
        if day in ["Sunday", "Saturday", "Friday", "Wednesday"]:
            self.label.setStyleSheet(f"background-color: {c}; color: white;")
        else:
            self.label.setStyleSheet(f"background-color: {c}; color: black;")

    def draw_shapes(self, c):
        canvas = self.canvas_label.pixmap()
        painter = QPainter(canvas)
        pen = QPen()

        pen.setColor(QColor("black"))
        pen.setWidth(1)
        pen.setStyle(Qt.PenStyle.SolidLine)
        painter.setPen(pen)

        brush = QBrush()
        brush.setColor(QColor(f"{c}"))
        brush.setStyle(Qt.BrushStyle.SolidPattern)
        painter.setBrush(brush)

        painter.drawEllipse(
            (int(canvas.width()) // 2) - (200 // 2),
            (int(canvas.height()) // 2) - (200 // 2),
            200, 200,
        )

        painter.end()
        self.canvas_label.setPixmap(canvas)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PaintingBoard()
    window.show()
    app.exec()
