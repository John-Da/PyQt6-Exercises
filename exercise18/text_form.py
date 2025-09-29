import sys
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QLineEdit,
    QTextEdit,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Text Input App")
        layout = QVBoxLayout()

        self.textInput = QLineEdit()
        self.addTextBtn = QPushButton("Add Text")
        self.addTextBtn.clicked.connect(self.add_text)
        self.textArea = QTextEdit()


        layout.addWidget(self.textInput)
        layout.addWidget(self.addTextBtn)
        layout.addWidget(self.textArea)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

        # Create widgets

        # Connect button click to method

        # Create layout and add widgets

        # Set up the central widget

    def add_text(self):
        # Get text from input field

        # Append text to text display

        # Clear the input field

        inputText = self.textInput.text()
        self.textArea.append(inputText)
        self.textInput.clear()

        pass


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())