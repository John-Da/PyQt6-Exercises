import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *


class Bounce(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Bounce Ball")
        self.setGeometry(400, 200, 400, 400)

        self.ball_container = QWidget()
        self.ball_container.setFixedSize(50, 50)

        self.ball = QLabel(self.ball_container)
        self.ball.setStyleSheet("background:red; border-radius: 15px;")
        self.ball.setFixedSize(30, 30)

        self.bounce_up = QPushButton("Bounce Up", self)
        self.bounce_down = QPushButton("Bounce Down", self)

        self.bounce_up.setMaximumWidth(100)
        self.bounce_up.setMaximumHeight(45)
        self.bounce_up.clicked.connect(self.bounceUp)

        self.bounce_down.setMaximumWidth(100)
        self.bounce_down.setMaximumHeight(45)
        self.bounce_down.clicked.connect(self.bounceDown)

        self.button_layout = QHBoxLayout()
        self.button_layout.addWidget(self.bounce_up)
        self.button_layout.addWidget(self.bounce_down)

        self.screen_layout = QVBoxLayout()
        self.screen_layout.addWidget(
            self.ball_container, alignment=Qt.AlignmentFlag.AlignCenter
        )
        self.screen_layout.addLayout(self.button_layout)

        container = QWidget()
        container.setLayout(self.screen_layout)
        self.setCentralWidget(container)

    def bounceUp(self):
        self.anim = QPropertyAnimation(self.ball_container, b"pos")
        self.anim.setDuration(500)
        self.anim.setEndValue(
            QPoint(self.ball_container.x(), self.ball_container.y() - 50)
        )
        self.anim.setEasingCurve(QEasingCurve.Type.OutBounce)
        self.anim.start()

    def bounceDown(self):
        self.anim = QPropertyAnimation(self.ball_container, b"pos")
        self.anim.setDuration(500)
        self.anim.setEndValue(
            QPoint(self.ball_container.x(), self.ball_container.y() + 50)
        )
        self.anim.setEasingCurve(QEasingCurve.Type.OutBounce)
        self.anim.start()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Bounce()
    window.show()
    app.exec()
