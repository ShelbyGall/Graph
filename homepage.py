from PyQt5.QtWidgets import (QApplication, 
                             QMainWindow, 
                             QPushButton, 
                             QLineEdit,
                             QVBoxLayout,
                             QHBoxLayout,
                             QWidget,
                             QFrame
                             )
from PyQt5.QtCore import QSize

import sys
from QVertex import QVertex


class MainWindow(QMainWindow):
    def __init__(self: QMainWindow):
        super().__init__()

        # set the title of the window
        self.setWindowTitle("Graph Visualization")

        # set the minimum size of the window
        self.setMinimumSize(QSize(1000,500))
        
        
        # create vertex button for action bar
        create_vertex_button = QPushButton("Create a Vertex")
        create_vertex_button.clicked.connect(self.create_vertex)

        # create graph button for action bar
        create_graph_button = QPushButton("Create a Graph")
        create_graph_button.clicked.connect(self.create_graph)

        # create the widget and layout for our action bar
        action_bar = QFrame()
        action_bar_layout = QVBoxLayout()

        # add our buttons to the action bar layout
        action_bar_layout.addWidget(create_vertex_button)
        action_bar_layout.addWidget(create_graph_button)

        # set the layout of our action bar
        action_bar.setLayout(action_bar_layout)


        # the graph VISUALIZATION stuff thingy
        canvas = QFrame()
        self.canvas_layout = QHBoxLayout()

        # line = QLineEdit()
        # self.canvas_layout.addWidget(line)

        canvas.setLayout(self.canvas_layout)



        # create the widget and layout for our main window container
        main_container = QFrame()
        main_container_layout = QHBoxLayout()

        # add our widgets to the layout
        main_container_layout.addWidget(action_bar)
        main_container_layout.addWidget(canvas)

        # set the layout of the main container
        main_container.setLayout(main_container_layout)

        # add the main container widget as the central widget
        self.setCentralWidget(main_container)

    def create_vertex(self):
        print("vertex created")
        v = QVertex()
        self.canvas_layout.addWidget(v)

    def create_graph(self):
        print("graph created")
        


if __name__ == '__main__':
    app = QApplication(sys.argv)

    with open("style.css", "r") as f:
        _style = f.read()
        app.setStyleSheet(_style)

    window = MainWindow()
    window.show()

    app.exec()