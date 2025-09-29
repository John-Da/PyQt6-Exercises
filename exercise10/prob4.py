from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
import sys


class MainWindow(QMainWindow):
    def __init__(self, name_id):
        super().__init__()

        self.name = name_id['name']
        self.id = name_id['id']

        self.setWindowTitle("My App")
        self.setFixedSize(QSize(300, 200))

        self.label = QLabel()
        self.input = QLineEdit()
        self.input.textChanged.connect(self.change_Text)

        
        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.label)


        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

    def change_Text(self):
        inputText = self.input.text()
        self.label.setText(f'{inputText}, {self.name} {self.id}')
        


app = QApplication(sys.argv)

name_id = {
    'name': 'Yen Da Hwa',
    'id': '7563'
}

window = MainWindow(name_id)

window.show()
app.exec()
