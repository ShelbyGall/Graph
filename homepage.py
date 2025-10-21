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

        # backend vertex being added to our graph
        v = Vertex.Vertex(label=str(self.vertex_counter))
        g.add_vertex(v)

        # GUI representation of our newly created vertex
        qv = QVertex(self.vertex_counter, id(v), x, y, 100, 100)
        self.addItem(qv)
        self.vertex_counter += 1

    
    def mouseReleaseEvent(self, event):
        # check it the button that triggered the event is the left mouse button
        # and that there is an item that is currently selected
        if event.button() == Qt.LeftButton and self.selectedItems():
            # check if the currently selected item and the last selected item are both QVertex's and they arent the same vertex
            if isinstance(self.selectedItems()[0], QVertex) and isinstance(self.last_selected_item, QVertex) and self.last_selected_item != self.selectedItems()[0]:
                # if we satisfy all conditions make an edge between the two vertices
                print(f"edge created\n{self.last_selected_item.v_label} -> {self.selectedItems()[0].v_label}")
                
                # TODO: add the edge to the actual backend graph 

                # TODO: add the visual representation of the edge to the scene (prolly gonna need to make a QEdge)

                # reset the bounding rectangle on the last selected vertex so its obvious that nothing
                # is currently selected
                tmp = self.selectedItems()[0]
                tmp.setEnabled(False)
                tmp.setEnabled(True)

                # reset selection status
                self.last_selected_item = None
                self.clearFocus()
                self.clearSelection()

            # if the last item selected wasnt a QVertex and the currently selected item is a QVertex
            elif self.selectedItems() and isinstance(self.selectedItems()[0], QVertex):
                # remember it so in the future we can check if the user wants to create an edge
                self.last_selected_item = self.selectedItems()[0]

            # if no conditions satisfy clear all selection settings
            else: 
                self.last_selected_item = None
                self.clearFocus()
                self.clearSelection()

        # if the either the click wasnt a left mouse click or there wasnt a selected item from the current
        # mouse press then revert the last selected item to None
        else:
            self.last_selected_item = None

        super().mouseReleaseEvent(event)
    



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
        create_graph_button = QPushButton("Delete Graph")
        create_graph_button.clicked.connect(self.delete_graph)

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

    def delete_graph(self):
        self.scene.clear()
        g = Graph.Graph([])
        self.scene.vertex_counter = 0
        print(g)


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