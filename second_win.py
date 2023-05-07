from PyQt5.QtCore import Qt, QTime, QTimer
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton, QLineEdit, QHBoxLayout
from PyQt5.QtGui import QFont
import instr as S
from final_win import FinalWin

class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.timer = QTimer()
        self.set_appear()
        self.inituI()
        self.connection()
        self.show()

    def set_appear(self):
        self.setWindowTitle(S.txt_title)
        self.resize(S.win_width, S.win_height)
        self.move(S.win_x,S.win_y)

    def inituI(self):
        self.fioText = QLabel(S.txt_name)
        self.ageText = QLabel(S.txt_age)
        self.inst1 = QLabel(S.txt_test1)
        self.inst2 = QLabel(S.txt_test2)
        self.inst3 = QLabel(S.txt_test3)
        self.timeText = QLabel(S.txt_timer)
        self.timeText.setFont(QFont("Times",36,QFont.Bold))


        self.buttoninst1 = QPushButton(S.txt_starttest1)
        self.buttoninst2 = QPushButton(S.txt_starttest2)
        self.buttoninst3 = QPushButton(S.txt_starttest3)
        self.buttonresult = QPushButton(S.txt_sendresults)

        self.editName = QLineEdit(S.txt_hintname)
        self.editAge = QLineEdit(S.txt_hintage)
        self.edit1 = QLineEdit(S.txt_hinttest1)
        self.edit2 = QLineEdit(S.txt_hinttest2)
        self.edit3 = QLineEdit(S.txt_hinttest3)

        self.LV1 = QVBoxLayout()
        self.LV1.addWidget(self.fioText, alignment=Qt.AlignLeft)
        self.LV1.addWidget(self.editName, alignment=Qt.AlignLeft)
        self.LV1.addWidget(self.ageText, alignment=Qt.AlignLeft)
        self.LV1.addWidget(self.editAge, alignment=Qt.AlignLeft)
        self.LV1.addWidget(self.inst1, alignment=Qt.AlignLeft)
        self.LV1.addWidget(self.buttoninst1, alignment=Qt.AlignLeft)
        self.LV1.addWidget(self.edit1, alignment=Qt.AlignLeft)
        self.LV1.addWidget(self.inst2, alignment=Qt.AlignLeft)
        self.LV1.addWidget(self.buttoninst2, alignment=Qt.AlignLeft)
        self.LV1.addWidget(self.inst3, alignment=Qt.AlignLeft)
        self.LV1.addWidget(self.buttoninst3, alignment=Qt.AlignLeft)
        self.LV1.addWidget(self.edit2, alignment=Qt.AlignLeft)
        self.LV1.addWidget(self.edit3, alignment=Qt.AlignLeft)
        self.LV1.addWidget(self.buttonresult, alignment=Qt.AlignLeft)

        main_line = QHBoxLayout()
        main_line.addLayout(self.LV1)
        main_line.addWidget(self.timeText, alignment=Qt.AlignCenter)

        self.setLayout(main_line)

    def connection(self):
        self.buttonresult.clicked.connect(self.next_click)
        self.buttoninst1.clicked.connect(self.test1)
        self.buttoninst2.clicked.connect(self.test2)
        self.buttoninst3.clicked.connect(self.test3)

    def test3(self):
        self.time = QTime(0,0,0)
        self.timeText.setText("00:00:00")
        self.timer.timeout.connect(self.last_test)
        self.timer.start(1000)

    def test1(self):
        self.time = QTime(0,0,15)
        self.timeText.setText("00:00:15")
        self.timer.timeout.connect(self.change_time)
        self.timer.start(1000)

    def test2(self):
        self.sit = 0
        self.timeText.setText(str(self.sit))
        self.timer.timeout.connect(self.add_sit)
        self.timer.start(1500)

    def last_test(self):
        if self.time.toString("hh:mm:ss") == "00:01:00":
            self.timer.stop()
        else:
            self.time = self.time.addSecs(1)
            if self.time.second() <=15 or self.time.second() >=45:
                self.timeText.setStyleSheet("color:rgb(0,255,0)")
            else:
                self.timeText.setStyleSheet("color:rgb(0,0,0)")

            self.timeText.setText(self.time.toString("hh:mm:ss"))
            self.timer.start(1000)

    def add_sit(self):
        self.timeText.setStyleSheet("color:rgb(0,0,0)")
        if self.sit == 30:
            self.timer.stop()
        else:
            self.sit += 1
            self.timeText.setText(str(self.sit))
            self.timer.start(1500)

    def change_time(self):
        self.timeText.setStyleSheet("color:rgb(0,0,0)")
        if self.time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()
        else:
            self.time = self.time.addSecs(-1)
            self.timeText.setText(self.time.toString("hh:mm:ss"))
            self.timer.start(1000)
        
    def next_click(self):
        self.hide()
        self.tw = FinalWin(self.editName.text,
                           int(self.editAge.text()),
                           (int(self.edit1.text())+
                           int(self.edit2.text())+
                           int(self.edit3.text())))