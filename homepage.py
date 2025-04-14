from PyQt5.QtWidgets import (QApplication, 
                             QMainWindow, 
                             QPushButton, 
                             QLabel, 
                             QLineEdit,
                             QVBoxLayout,
                             QWidget,
                             )
from PyQt5.QtCore import QSize

import sys

class MainWindow(QMainWindow):
    def __init__(self: QMainWindow):
        super().__init__()

        # set the title of the window
        self.setWindowTitle("Graph Visualization")

        # set the minimum size of the window
        self.setMinimumSize(QSize(500,300))
        # create a layout and add it ass the central widget of the window
        self.layout = QVBoxLayout()

        self.label = QLabel()
        self.input = QLineEdit()
        self.input.textChanged.connect(self.label.setText)

        self.button = QPushButton("Create a Vertex")
        self.button.clicked.connect(self.create_vertex_button)

        self.layout.addWidget(self.input)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.button)

        self.container = QWidget()
        self.container.setLayout(self.layout)
        
    

        self.setCentralWidget(self.container)


    def create_vertex_button(self):
        print("vertex created")

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()