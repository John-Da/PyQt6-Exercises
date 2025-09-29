from PyQt6 import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
import sys


class Color(QWidget):
    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Color Mixer")
        self.setFixedSize(QSize(400, 600))

        self.red_label = QLabel("Red")
        self.red = QSlider(Qt.Orientation.Horizontal)
        self.red.setMinimum(0)
        self.red.setMaximum(255)
        self.red.setValue(0)
        self.red.valueChanged.connect(self.update_color)

        self.green_label = QLabel("Green")
        self.green = QSlider(Qt.Orientation.Horizontal)
        self.green.setMinimum(0)
        self.green.setMaximum(255)
        self.green.setValue(0)
        self.green.valueChanged.connect(self.update_color)

        self.blue_label = QLabel("Blue")
        self.blue = QSlider(Qt.Orientation.Horizontal)
        self.blue.setMinimum(0)
        self.blue.setMaximum(255)
        self.blue.setValue(0)
        self.blue.valueChanged.connect(self.update_color)

        self.sliders = [self.red, self.green, self.blue]

        self.color_label = QLabel()
        self.color_label.setStyleSheet(f"background-color:rgb(0,0,0)")

        layout = QVBoxLayout()
        layout.addWidget(self.red_label)
        layout.addWidget(self.red)
        layout.addWidget(self.green_label)
        layout.addWidget(self.green)
        layout.addWidget(self.blue_label)
        layout.addWidget(self.blue)
        layout.addWidget(self.color_label)

        self.color_label.setFixedSize(300, 300)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def update_color(self):
        r, g, b = [slider.value() for slider in self.sliders]
        self.color_label.setStyleSheet(f"background-color:rgb({r}, {g}, {b})")


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
