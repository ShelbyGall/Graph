from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QPushButton, QFrame

class QVertex(QtWidgets.QFrame):
    

    def __init__(self):
        super().__init__()
        layout = QtWidgets.QGridLayout()
        b1 = QPushButton("Label")
        b2 = QPushButton("Data")
        b3 = QPushButton("Add Edge")
        delete_vertex_button = QPushButton("Delete Vertex")

        delete_vertex_button.clicked.connect(self.delete_vertex)
        layout.addWidget(b1, 0, 0)
        layout.addWidget(b2, 1, 0)
        layout.addWidget(b3, 0, 1)
        layout.addWidget(delete_vertex_button, 1, 1)

        self.setLayout(layout)

    def delete_vertex(self):
        # delete GUI representation of node
        self.setParent(None)
        # TODO: delete node from the GUI
    
    
    