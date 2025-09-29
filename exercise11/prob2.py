from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Information of 663040756-3")
        self.setFixedSize(QSize(500, 200))

        self.label = QLabel("Yen Da Hwa")
        font = self.label.font()
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setAlignment(
            Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter
        )

        self.checklist1 = QCheckBox("Orange Juice")
        self.checklist2 = QCheckBox("Green Tea")
        self.checklist1.stateChanged.connect(self.chl1)
        self.checklist2.stateChanged.connect(self.chl2)

        self.comboList = QComboBox()
        self.comboList.addItems(["COE", "DME"])
        self.comboList.currentTextChanged.connect(self.combotext)

        self.statusLabel = QLabel("Status:", self)
        font = self.statusLabel.font()
        font.setPointSize(20)
        self.statusLabel.setFont(font)
        self.statusLabel.setAlignment(
            Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter
        )
        self.statusLabel.setStyleSheet('background-color: "#caeda8"; color: black')

        self.quitbtn = QPushButton("Quit")
        self.quitbtn.clicked.connect(QApplication.instance().quit)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.checklist1)
        layout.addWidget(self.checklist2)
        layout.addWidget(self.comboList)
        layout.addWidget(self.statusLabel)
        layout.addWidget(self.quitbtn)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

    def chl1(self, value):
        cm1 = "You want to drink Orange Juice"
        cm3 = "You don't want to drink Orange Juice"

        state = Qt.CheckState(value)

        if state == Qt.CheckState.Checked:
            self.statusLabel.setText(cm1)

        else:
            self.statusLabel.setText(cm3)

    def chl2(self, value):
        cm2 = "You want to drink Green Tea"
        cm4 = "You don't want to drink Green Tea"

        state = Qt.CheckState(value)

        if state == Qt.CheckState.Checked:
            self.statusLabel.setText(cm2)

        else:
            self.statusLabel.setText(cm4)

    def combotext(self, i):
        cbm1 = "You have studied in COE"
        cbm2 = "You have studied in DME"

        if i == "COE":
            self.statusLabel.setText(cbm1)
        elif i == "DME":
            self.statusLabel.setText(cbm2)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
