from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Checkbox and ComboBox")
        self.setFixedSize(QSize(500, 200))

        self.label = QLabel()

        self.checklist1 = QCheckBox("Enable ComboBox")
        self.checklist1.stateChanged.connect(self.chl1)

        self.comboList = QComboBox()
        self.comboList.addItems(["Option 1", "Option 2", "Option 3"])
        self.comboList.setEnabled(False)
        self.comboList.currentTextChanged.connect(self.enableCombo)

        layout = QVBoxLayout()
        layout.addWidget(self.checklist1)
        layout.addWidget(self.comboList)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

    def chl1(self, value):
        state = Qt.CheckState(value)
        if state == Qt.CheckState.Checked:
            self.comboList.setEnabled(True)
        else:
            self.comboList.setEnabled(False)

    def enableCombo(self, item):
        print(f"Selected item: {item}")


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
