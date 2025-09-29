from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
import sys


class WordCounter(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Word Counter")
        self.setFixedSize(QSize(300, 200))

        self.label = QLabel('Word count: 0')
        
        self.input = QLineEdit()
        self.input.textChanged.connect(self.wordCount)

        
        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.label)


        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

    def wordCount(self):
        inputText = self.input.text().strip().split()
        count = len(inputText)
        self.label.setText(f'Word count: {count}')
        


app = QApplication(sys.argv)
counter = WordCounter()
counter.show()
app.exec()
