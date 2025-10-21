from PyQt5.QtWidgets import (QApplication, 
                             QMainWindow, 
                             QPushButton, 
                             QGraphicsScene,
                             QGraphicsView,
                             QVBoxLayout,
                             QWidget,
                             QDockWidget,
                             QAction
                             )
from PyQt5.QtCore import QSize, Qt

from PyQt5.QtGui import QIcon

import math
import sys
from QVertex import QVertex

import Graph
import Vertex

g = Graph.Graph([])

class QGraphicsScene(QGraphicsScene):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.last_selected_item = None
        self.vertex_counter = 0

    def mouseDoubleClickEvent(self, event):
        print("vertex created")
        
        x = event.scenePos().x() - 50
        y = event.scenePos().y() - 50

        v = Vertex.Vertex(label=str(self.vertex_counter))
        g.add_vertex(v)

        # GUI representation of our newly created vertex
        qv = QVertex(self.vertex_counter, id(v), x, y, 100, 100)

        

        self.addItem(qv)
        self.vertex_counter += 1

    
    def mousePressEvent(self, event):
        # print(f"self: {self}")
        # print(f"event: {event}")
        if event.button() == Qt.LeftButton:
            if self.selectedItems():
                print(self.selectedItems()[0])
        super().mousePressEvent(event)
    



class MainWindow(QMainWindow):
    def __init__(self: QMainWindow):
        super().__init__()

        # set the title of the window
        self.setWindowTitle("Graph Visualization")

        # set the window icon
        self.setWindowIcon(QIcon('./assets/icon.png'))

        # set the minimum size of the window
        self.setMinimumSize(QSize(1000,500))

        # create the menu bar
        menu_bar = self.menuBar()

        # add items to the menu bar
        help_menu = menu_bar.addMenu('&Help')
        view_menu = menu_bar.addMenu('&View')

        # help menu actions
        about_action = QAction(QIcon('./assets/about.png'), 'About', self)
        help_menu.addAction(about_action)
        about_action.setStatusTip('About')
        about_action.setShortcut('F1')

        # view menu actions
        show_dock_action = QAction(QIcon('./assets/show_dock.png'), 'Show Dock Widget', self)
        show_dock_action.triggered.connect(self.show_dock)
        show_dock_action.setStatusTip('Show Dock Widget')
        show_dock_action.setShortcut('F2')
        view_menu.addAction(show_dock_action)

        # create graph button for dock widget
        create_graph_button = QPushButton("Create a Graph")
        create_graph_button.clicked.connect(self.create_graph)

        # create a dock widget for our graph options
        self.dock = QDockWidget('Graph Options')

        # create widget for our multiple graph option actions
        graph_options = QWidget()
        graph_options_layout = QVBoxLayout()
        graph_options.setLayout(graph_options_layout)
        graph_options_layout.addWidget(create_graph_button)

        # set the widget for the dock widget
        self.dock.setWidget(graph_options)

        # add the dock widget to the app
        self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, self.dock)

        # the graph VISUALIZATION stuff thingy
        self.scene = QGraphicsScene(0,0,400,200)

        view = QGraphicsView(self.scene)

        self.setCentralWidget(view)

    def create_graph(self):
        print("graph created")

    def show_dock(self):
        self.dock.show()

    def do_sum(self):
        print("doin sum")

if __name__ == '__main__':
    app = QApplication(sys.argv)

    with open("style.css", "r") as f:
        _style = f.read()
        app.setStyleSheet(_style)

    window = MainWindow()
    window.show()

    app.exec()