from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QPushButton, QFrame

class QVertex(QtWidgets.QFrame):
    
    def __init__(self):
        super().__init__()
        layout = QtWidgets.QGridLayout()
        
        b1 = QPushButton("B1")
        b2 = QPushButton("B2")
        b3 = QPushButton("B3")
        b4 = QPushButton("B4")
        layout.addWidget(b1, 0, 0)
        layout.addWidget(b2, 1, 0)
        layout.addWidget(b3, 0, 1)
        layout.addWidget(b4, 1, 1)

        self.setLayout(layout)
        