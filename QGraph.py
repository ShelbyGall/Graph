from PyQt5.QtWidgets import (QGraphicsItem, 
                             QMenu, 
                             QAction, 
                             QGraphicsTextItem, 
                             QGraphicsEllipseItem, 
                             QGraphicsLineItem,
                             )
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QPoint
import math


class QVertex(QGraphicsEllipseItem):
    def __init__(self, label, id, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # store the label of the vertex 
        self.v_label = label

        # store the python id of the vertex
        self.v_id = id

        # make the QVertex moveable and selectable
        self.setFlag(QGraphicsItem.ItemIsMovable)
        self.setFlag(QGraphicsItem.ItemIsSelectable)
        
        # create the text label for the QVertex object
        self.label = QGraphicsTextItem(str(self.v_label), self)

        # set the position of the label on the QVertex in the GUI
        self.label.setPos(args[0]+45, args[1]+40)

    def contextMenuEvent(self, event):
        context_menu = QMenu()
        context_menu.setWindowIconText(str(self.v_label))

        # SELF IS THE VERTEX THAT WAS RIGHT CLICKED ON, MAKE 
        # SURE YOU PASS IT ACCORDINGLY
        view_id = QAction(QIcon('./assets/id.png'), f'Vertex ID | {self.v_id}')
        view_id.setDisabled(True)
        context_menu.addAction(view_id)

        context_menu.addSeparator()

        update = QAction(QIcon('./assets/update.png'), 'Update Label')
        update.triggered.connect(lambda _ : self.label.setPlainText('ur gay'))
        context_menu.addAction(update)

        add_edge = QAction(QIcon('./assets/edge.png'), 'Add an Edge')
        add_edge.triggered.connect(lambda _ : print("added edge"))
        context_menu.addAction(add_edge)

        x = math.floor(event.scenePos().x()) + 235
        y = math.floor(event.scenePos().y()) + 75
        point= event.widget().mapToGlobal(QPoint(x,y))

        context_menu.exec_(point)

    
    def setLabel(self, new_label):
        self.v_label = new_label

class QEdge(QGraphicsLineItem):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        