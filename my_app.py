from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout,QPushButton, QApplication
import instr as S

class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.inituI()
        self.connection()
        self.show()

    def set_appear(self):
        self.setWindowTitle(S.txt_title)
        self.resize(S.win_width, S.win_height)
        self.move(S.win_x,S.win_y)

    def inituI(self):
        self.helo_txt = QLabel(S.txt_hello)
        self.instruction = QLabel(S.txt_instruction)
        self.button = QPushButton(S.txt_next)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.helo_txt, alignment=Qt.AlignCenter)
        self.layout.addWidget(self.instruction, alignment=Qt.AlignCenter)
        self.layout.addWidget(self.button, alignment=Qt.AlignCenter)
        self.setLayout(self.layout)

    def connection(self):
        self.button.clicked.connect(self.next_click)

    def next_click(self):
        self.hide()
        #self.tw = TestWin()

app = QApplication([])
mw = MainWin()
app.exec_()
