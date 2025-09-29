from PyQt6 import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Volume Control")
        self.size_and_center(200, 100)

        self.slider = QSlider(Qt.Orientation.Horizontal)
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)
        self.slider.setValue(50)
        self.slider.valueChanged.connect(self.display)

        self.value_label = QLabel("50%")
        self.value_label.setAlignment(
            Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter
        )

        self.button = QPushButton("Mute")
        self.button.clicked.connect(self.click_btn)

        layout = QVBoxLayout()
        layout.addWidget(self.slider)
        layout.addWidget(self.value_label)
        layout.addWidget(self.button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def size_and_center(self, width, height):
        screen = QApplication.primaryScreen().geometry()
        x = (screen.width() - width) // 2
        y = (screen.height() - height) // 2
        self.setGeometry(x, y, width, height)

    def display(self):
        self.value_label.setText(str(self.sender().value()) + "%")
        self.value_label.adjustSize()

    def click_btn(self):
        self.slider.setValue(0)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
