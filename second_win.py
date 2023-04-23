from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QMessageBox
from PyQt5.QtCore import Qt
import instr as T

app = QApplication([])

window = QWidget()
window.move(T.win_x, T.win_y)
window.resize(T.win_width, T.win_height)
window.setWindowTitle(T.txt_title)

LV1 = QVBoxLayout()
fioText = QLabel(T.txt_name)
ageText = QLabel(T.txt_age)
inst1 = QLabel(T.txt_test1)
inst2 = QLabel(T.txt_test2)
inst3 = QLabel(T.txt_test3)

buttoninst1 = QPushButton(T.txt_starttest1)
buttoninst2 = QPushButton(T.txt_starttest2)
buttoninst3 = QPushButton(T.txt_starttest3)
buttonresult = QPushButton(T.txt_sendresults)

LV1.addWidget(fioText, alignment=Qt.AlignLeft)
LV1.addWidget(ageText, alignment=Qt.AlignLeft)
LV1.addWidget(inst1, alignment=Qt.AlignLeft)
LV1.addWidget(inst2, alignment=Qt.AlignLeft)
LV1.addWidget(inst3, alignment=Qt.AlignLeft)
LV1.addWidget(buttoninst1, alignment=Qt.AlignLeft)
LV1.addWidget(buttoninst2, alignment=Qt.AlignLeft)
LV1.addWidget(buttoninst3, alignment=Qt.AlignLeft)
LV1.addWidget(buttonresult, alignment=Qt.AlignLeft)

LV2 = QVBoxLayout()
timeText = QLabel(T.txt_timer)
LV2.addWidget(timeText, alignment=Qt.AlignCenter)

main_line = QHBoxLayout()
main_line.addLayout(LV1)
main_line.addLayout(LV2)

window.setLayout(main_line)

window.show()
app.exec_()
