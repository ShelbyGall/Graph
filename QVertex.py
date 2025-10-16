from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QGraphicsItem, QMenu, QAction
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QPoint
import math


class QVertex(QtWidgets.QGraphicsEllipseItem):
    

    def __init__(self):
        super().__init__(0,0,100,100)
        
        self.setFlag(QGraphicsItem.ItemIsMovable)
        self.setFlag(QGraphicsItem.ItemIsSelectable)

    def delete_vertex(self):
        # delete GUI representation of node
        print(self.parentItem())
        print(self.parentWidget())
        print(self.parentObject())
        # TODO: delete node from the GUI

    def contextMenuEvent(self, event):
        print("here")
        print(self)
        context_menu = QMenu()

        delete = QAction(QIcon('./assets/delete.png'), 'Delete Vertex')
        delete.triggered.connect(lambda _ : print("delete vertex"))
        context_menu.addAction(delete)

        add_edge = QAction(QIcon('./assets/edge.png'), 'Add an Edge')
        add_edge.triggered.connect(lambda _ : print("added edge"))
        context_menu.addAction(add_edge)

        q_point_f = self.mapToParent(event.pos())
        print(q_point_f)
        x = math.floor(q_point_f.x())
        y = math.floor(q_point_f.y())
        print(f"{x}, {y}")
        context_menu.exec_(QPoint(x,y))

