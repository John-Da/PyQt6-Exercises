from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        self.setFixedSize(QSize(500, 200))

        self.label = QLabel()
        font = self.label.font()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setStyleSheet("background:yellow; color:black;")

        self.input = QLineEdit()
        self.input.returnPressed.connect(self.printItemText)

        self.listWidget = QListWidget()
        self.listWidget.setSelectionMode(QAbstractItemView.SelectionMode.MultiSelection)

        itemlist = ["EN842300", "EN842314", "EN842315"]
        for i in range(len(itemlist)):
            items = QListWidgetItem(itemlist[i])
            self.listWidget.addItem(items)
        self.listWidget.itemClicked.connect(self.printItemText)

        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.listWidget)
        layout.addWidget(self.label)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

    def printItemText(self):
        inputtext = self.input.text().strip()

        items = [item.text() for item in self.listWidget.selectedItems()]
        for i in range(self.listWidget.count()):
            item = self.listWidget.item(i)
            item.setBackground(Qt.GlobalColor.black)

        if items:
            for item in self.listWidget.selectedItems():
                item.setBackground(Qt.GlobalColor.yellow)
            if inputtext:
                self.label.setText(
                    f'Hello {inputtext}! You are interested in these courses {",".join(map(str, items))}'
                )
            else:
                self.label.setText(f"You are interested in these courses {', '.join(items)}")
        else:
            if inputtext:
                self.label.setText(f'Hello {inputtext}!{", ".join(items)}')
            else:
                self.label.setText("")


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
