from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
import sys


class MainWindow(QMainWindow):
    def __init__(self, name, id):
        super().__init__()

        self.stName = name
        self.stId = id

        self.setWindowTitle(self.stName)
        self.setFixedSize(QSize(300, 200))

        self.button_text = 'Click me'
        self.button = QPushButton(self.button_text)
        self.button.setCheckable(False)
        self.button.clicked.connect(self.click_btn)
        self.setCentralWidget(self.button)
    
    def click_btn(self):
        self.button.setText(self.stId)
        self.button.setEnabled(False)
        self.setWindowTitle(self.stId)
            



app = QApplication(sys.argv)

student = {
    'name': 'Yen Da Hwa',
    'id': '663040756-3'
}

window = MainWindow(student['name'], student['id'])
window.show()
app.exec()
