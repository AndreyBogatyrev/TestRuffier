from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton, QLineEdit, QHBoxLayout
from PyQt5.QtGui import QFont
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

        self.timer = QTimer()

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
        self.timeText = QLabel(S.txt_timer)
        self.timeText.setFont(QFont('Times', 36, QFont.Bold))
        self.LV2.addWidget(self.timeText, alignment=Qt.AlignCenter)

        main_line = QHBoxLayout()
        main_line.addLayout(self.LV1)
        main_line.addLayout(self.LV2)

        self.setLayout(main_line)

    def connection(self):
        self.buttoninst1.clicked.connect(self.timer_test1)
        self.buttoninst2.clicked.connect(self.timer_test2)
        self.buttoninst3.clicked.connect(self.timer_test3)

        self.buttonresult.clicked.connect(self.next_click)
        self.editName.editingFinished.connect(self.SetName)
        self.editAge.editingFinished.connect(self.SetAge)
        self.edit1.editingFinished.connect(self.SetRes1)
        self.edit2.editingFinished.connect(self.SetRes2)
        self.edit3.editingFinished.connect(self.SetRes3)

    def next_click(self):
        self.hide()
        self.tw = FinalWin(self.Name, self.age, self.edit1, self.edit2, self.edit3)

    def SetAge(self):
        self.age = int(self.editAge.text())
    def SetRes1(self):
        self.Res1 = int(self.edit1.text())
    def SetRes2(self):
        self.Res2 = int(self.edit2.text())
    def SetRes3(self):
        self.Res3 = int(self.edit3.text())
    
    def SetName(self):
        self.Name = self.editName.text()

    def timer_test1(self):
        global time
        time = QTime(0, 1, 0)
        self.timer.timeout.connect(self.timer1Event)
        self.timer.start(1000) # 1000

    def timer_test2(self):
        global time
        time = QTime(0, 0, 30)
        self.timer.timeout.connect(self.timer2Event)
        self.timer.start(1500) # 1500

    def timer_test3(self):
        global time
        time = QTime(0, 1, 0)
        self.timer.timeout.connect(self.timer3Event)
        self.timer.start(1000) # 1000

    def timer1Event(self):
        global time
        time = time.addSecs(-1)
        self.timeText.setText(time.toString('hh:mm:ss'))
        self.timeText.setStyleSheet('color: rgb(0, 0, 0)')
        if time.toString('hh:mm:ss') == '00:00:00':
            self.timer.stop()
            self.timer.timeout.disconnect()

    def timer2Event(self):
        global time
        time = time.addSecs(-1)
        self.timeText.setText(time.toString('hh:mm:ss')[6:8])
        self.timeText.setStyleSheet('color: rgb(0, 0, 0)')
        if self.timeText.text() == '00':
            self.timer.stop()
            self.timer.timeout.disconnect()

    def timer3Event(self):
        global time
        time = time.addSecs(-1)
        self.timeText.setText(time.toString('hh:mm:ss'))

        if int(time.toString('hh:mm:ss')[6:8]) >= 45:
            self.timeText.setStyleSheet('color: rgb(0, 255, 0)')
        elif int(time.toString('hh:mm:ss')[6:8]) <= 15:
            self.timeText.setStyleSheet('color: rgb(0, 255, 0)')
        else:
            self.timeText.setStyleSheet('color: rgb(0, 0, 0)')
        
        if time.toString('hh:mm:ss') == '00:00:00':
            self.timer.stop()
            self.timer.timeout.disconnect()