from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout,QPushButton, QApplication
import instr as S

def GetStatus(index, age):
    if age >= 15 and index >=15:
        return "Низкий"
    elif 13 <= age <= 14 and index >=16.5:
        return "Низкий"    
    elif 11 <= age <= 12 and index >=18:
        return "Низкий"
    elif 9 <= age <= 10 and index >=19.5:
        return "Низкий"
    elif 7 <= age <= 8 and index >= 21:
        return "Низкий"
    else:
        return "Высокий"


class FinalWin(QWidget):
    def __init__(self, name, age, sumP):
        super().__init__()
        self.age = age
        self.Ruffie = (4*sumP-200)/10
        self.set_appear()
        self.inituI()
        self.show()

    def set_appear(self):
        self.setWindowTitle(S.txt_finalwin)
        self.resize(S.win_width, S.win_height)
        self.move(S.win_x,S.win_y)

    def inituI(self):
        self.index = QLabel(S.txt_index+str(self.Ruffie))
        self.workheart = QLabel(S.txt_workheart + GetStatus(self.Ruffie, self.age))
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.index, alignment=Qt.AlignCenter)
        self.layout.addWidget(self.workheart, alignment=Qt.AlignCenter)
        self.setLayout(self.layout)