from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QGraphicsItem, QMenu, QAction, QGraphicsTextItem
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QPoint, QPointF
import math


class QVertex(QtWidgets.QGraphicsEllipseItem):
    def __init__(self, label, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.v_label = label
        self.v_data = None

        self.setFlag(QGraphicsItem.ItemIsMovable)
        self.setFlag(QGraphicsItem.ItemIsSelectable)
        
        self.label = QGraphicsTextItem(str(self.v_label), self)
        self.label.setPos(args[0]+45, args[1]+40)
        
        

    def contextMenuEvent(self, event):
        context_menu = QMenu()
        context_menu.setWindowIconText(str(self.v_label))

        delete = QAction(QIcon('./assets/update.png'), 'Update Label')
        delete.triggered.connect(lambda _ : self.label.setPlainText('ur gay'))
        context_menu.addAction(delete)

        add_edge = QAction(QIcon('./assets/edge.png'), 'Add an Edge')
        add_edge.triggered.connect(lambda _ : print("added edge"))
        context_menu.addAction(add_edge)

        x = math.floor(event.scenePos().x())
        y = math.floor(event.scenePos().y())
        context_menu.exec_(QPoint(x,y))

    def setLabel(self, new_label):
        self.v_label = new_label

