from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.choices = []


        self.setWindowTitle("Context Menu Font Style")
        self.setFixedSize(QSize(500, 200))

        self.label = QLabel('Right-click to change font style')
        self.label.setAlignment(
            Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter
        )

        layout = QVBoxLayout()
        layout.addWidget(self.label)


        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

    def contextMenuEvent(self, e):
        context = QMenu(self)
        context.addAction(QAction('Bold', self))
        context.addAction(QAction('Italic', self))
        context.triggered.connect(self.menu_choice)
        context.exec(e.globalPos())

    def menu_choice(self, action):
        if action.text() == 'Bold':
            self.label.setStyleSheet('font: bold')
        elif action.text() == 'Italic':
            self.label.setStyleSheet('font: italic')
  


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
