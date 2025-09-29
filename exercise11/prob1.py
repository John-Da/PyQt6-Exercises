from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("663040756-3")
        self.setFixedSize(QSize(300, 200))

        self.label = QLabel("Yen Da Hwa")

        self.quitbtn = QPushButton("Quit")
        self.quitbtn.clicked.connect(QApplication.instance().quit)
        self.quitbtn.setToolTip("Click to quit")

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.quitbtn)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

    def closeEvent(self, event):
        reply = QMessageBox.question(
            self,
            "Message",
            "Are you sure to quit?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No,
        )
        if reply == QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
