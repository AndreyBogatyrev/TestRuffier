from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton, QLineEdit, QHBoxLayout
import instr as S
from final_win import FinalWin

class TestWin(QWidget):
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
        self.LV1 = QVBoxLayout()
        self.fioText = QLabel(S.txt_name)
        self.ageText = QLabel(S.txt_age)
        self.inst1 = QLabel(S.txt_test1)
        self.inst2 = QLabel(S.txt_test2)
        self.inst3 = QLabel(S.txt_test3)

        self.buttoninst1 = QPushButton(S.txt_starttest1)
        self.buttoninst2 = QPushButton(S.txt_starttest2)
        self.buttoninst3 = QPushButton(S.txt_starttest3)
        self.buttonresult = QPushButton(S.txt_sendresults)

        self.editName = QLineEdit(S.txt_hintname)
        self.editAge = QLineEdit(S.txt_hintage)
        self.edit1 = QLineEdit(S.txt_hinttest1)
        self.edit2 = QLineEdit(S.txt_hinttest2)
        self.edit3 = QLineEdit(S.txt_hinttest3)

        self.LV1.addWidget(self.fioText, alignment=Qt.AlignLeft)
        self.LV1.addWidget(self.editName, alignment=Qt.AlignLeft)
        self.LV1.addWidget(self.ageText, alignment=Qt.AlignLeft)
        self.LV1.addWidget(self.editAge, alignment=Qt.AlignLeft)
        self.LV1.addWidget(self.inst1, alignment=Qt.AlignLeft)
        self.LV1.addWidget(self.buttoninst1, alignment=Qt.AlignLeft)
        self.LV1.addWidget(self.edit1, alignment=Qt.AlignLeft)
        self.LV1.addWidget(self.inst2, alignment=Qt.AlignLeft)
        self.LV1.addWidget(self.buttoninst2, alignment=Qt.AlignLeft)
        self.LV1.addWidget(self.edit2, alignment=Qt.AlignLeft)
        self.LV1.addWidget(self.inst3, alignment=Qt.AlignLeft)
        self.LV1.addWidget(self.buttoninst3, alignment=Qt.AlignLeft)
        self.LV1.addWidget(self.edit3, alignment=Qt.AlignLeft)
        self.LV1.addWidget(self.buttonresult, alignment=Qt.AlignLeft)

        self.LV2 = QVBoxLayout()
        timeText = QLabel(S.txt_timer)
        self.LV2.addWidget(timeText, alignment=Qt.AlignCenter)

        main_line = QHBoxLayout()
        main_line.addLayout(self.LV1)
        main_line.addLayout(self.LV2)

        self.setLayout(main_line)

    def connection(self):
        self.buttonresult.clicked.connect(self.next_click)

    def next_click(self):
        self.hide()
        self.tw = FinalWin(60, 15)
