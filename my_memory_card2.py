from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, QPushButton, QLabel)


app = QApplication([]) 


window = QWidget()
window.setWindowTitle('Memory Card')

qb1 = QLabel("Question")
qb2 = QLabel("Test Result")
qb3 = QLabel("True/False")
qb4 = QLabel("Correct Answer")
qgb = QGroupBox()
nq = QPushButton("Next Question")

HL1 = QHBoxLayout() # For big question
HL1.addWidget(qb1, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))

HL2 = QHBoxLayout() # For button NQ
HL2.addWidget(nq)


VL1 = QVBoxLayout() # inside qgb
VL1.addWidget(qb3)
VL1.addWidget(qb4)
qgb.setLayout(VL1)



VL2 = QVBoxLayout() 
VL2.addLayout(HL1)
VL2.addWidget(qb2)
VL2.addWidget(qgb)
VL2.addLayout(HL2)


window.setLayout(VL2)
window.show()
app.exec()

