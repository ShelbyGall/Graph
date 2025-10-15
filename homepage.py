from PyQt5.QtWidgets import (QApplication, 
                             QMainWindow, 
                             QPushButton, 
                             QLineEdit,
                             QVBoxLayout,
                             QHBoxLayout,
                             QWidget,
                             QFrame,
                             QDockWidget,
                             QAction
                             )
from PyQt5.QtCore import QSize, Qt

from PyQt5.QtGui import QIcon


import sys
from QVertex import QVertex


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


        # create vertex button for action bar
        create_vertex_button = QPushButton("Create a Vertex")
        create_vertex_button.clicked.connect(self.create_vertex)

        # create graph button for action bar
        create_graph_button = QPushButton("Create a Graph")
        create_graph_button.clicked.connect(self.create_graph)

        # create a dock widget for our graph options
        self.dock = QDockWidget('Graph Options')

        # create widget for our multiple graph option actions
        graph_options = QWidget()
        graph_options_layout = QVBoxLayout()
        graph_options.setLayout(graph_options_layout)
        graph_options_layout.addWidget(create_graph_button)
        graph_options_layout.addWidget(create_vertex_button)

        # the graph VISUALIZATION stuff thingy
        canvas = QFrame()
        canvas.setObjectName("canvas")
        self.canvas_layout = QHBoxLayout()



        canvas.setLayout(self.canvas_layout)



        # create the widget and layout for our main window container
        main_container = QFrame()
        main_container.setObjectName("main_container")
        main_container_layout = QHBoxLayout()

        # add our widgets to the layout
        self.dock.setWidget(graph_options)
        self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, self.dock)
        main_container_layout.addWidget(canvas,4)

        # set the layout of the main container
        main_container.setLayout(main_container_layout)

        # add the main container widget as the central widget
        self.setCentralWidget(main_container)

    def create_vertex(self):
        print("vertex created")
        v = QVertex()
        v.setObjectName('vertex') 
        self.canvas_layout.addWidget(v)

    def create_graph(self):
        print("graph created")

    def show_dock(self):
        self.dock.show()

        


if __name__ == '__main__':
    app = QApplication(sys.argv)

    with open("style.css", "r") as f:
        _style = f.read()
        app.setStyleSheet(_style)

    window = MainWindow()
    window.show()

    app.exec()