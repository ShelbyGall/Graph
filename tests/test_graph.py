import sys
sys.path.append('./')

import unittest
import warnings

import Vertex as V
import Graph as G

# TODO: Turn all these code blocks below into unit tests 
class TestGraph(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.v1 = V.Vertex('1')
        cls.v2 = V.Vertex('2')
        cls.v3 = V.Vertex('3')
        cls.v4 = V.Vertex('4')
        cls.v5 = V.Vertex('5')
        cls.v6 = V.Vertex('6')
        cls.v7 = V.Vertex('7')
        cls.v8 = V.Vertex('8')

        cls.vertices = [cls.v1,
                        cls.v2,
                        cls.v3,
                        cls.v4]
        cls.no_edge_graph = G.Graph(vertices=cls.vertices)

        cls.pop_edge_graph = G.Graph(vertices=cls.vertices)

        cls.pop_edge_graph.add_edge(src=cls.v1, dest=cls.v3, directed=False)
        cls.pop_edge_graph.add_edge(src=cls.v3, dest=cls.v2)
        cls.pop_edge_graph.add_edge(src=cls.v4, dest=cls.v1)
        cls.pop_edge_graph.add_edge(src=cls.v1, dest=cls.v3, directed=False)
        cls.pop_edge_graph.add_edge(src=cls.v3, dest=cls.v2)
        cls.pop_edge_graph.add_edge(src=cls.v4, dest=cls.v1)

        cls.vertices2 = [cls.v1,cls.v2,cls.v3,cls.v4,cls.v5,cls.v6,cls.v7,cls.v8]
        cls.g2 = G.Graph(vertices=cls.vertices2)

        cls.g2.add_edge(src=cls.v1, dest=cls.v2, directed=False)
        cls.g2.add_edge(src=cls.v1, dest=cls.v3, directed=False)
        cls.g2.add_edge(src=cls.v1, dest=cls.v4, directed=False)
        cls.g2.add_edge(src=cls.v3, dest=cls.v6, directed=False)
        cls.g2.add_edge(src=cls.v3, dest=cls.v7, directed=False)
        cls.g2.add_edge(src=cls.v4, dest=cls.v7, directed=False)
        cls.g2.add_edge(src=cls.v6, dest=cls.v8, directed=False)

    def test_no_edge_graph_init(self):
        self.assertTrue(hasattr(self.no_edge_graph, "vertices"))
        self.assertTrue(hasattr(self.no_edge_graph, "edges"))

        self.assertIsInstance(self.no_edge_graph, G.Graph)
        self.assertIsInstance(self.vertices, list)
        self.assertEqual(self.no_edge_graph.edges, {self.v1:[],
                                                    self.v2:[],
                                                    self.v3:[],
                                                    self.v4:[],})

    def test_add_edge(self):
        with warnings.catch_warnings():
            warnings.simplefilter('always')
            with self.assertWarns(UserWarning) as uw:
                self.pop_edge_graph.add_edge(src=self.v5, dest=self.v2)
            
            self.assertEqual("Error: Vertices ['5'] not in Graph", str(uw.warning))

            with self.assertWarns(UserWarning) as uw:
                self.pop_edge_graph.add_edge(src=self.v5, dest=self.v6, directed=False)
            
            self.assertEqual("Error: Vertices ['5', '6'] not in Graph", str(uw.warning))


    def test_bfs(self):
        self.g2.bfs(self.v1,self.v8)


# print()
# g2.dfs(self.v1,self.v8)
# print()
# g2.dfs_recursive(self.v1,self.v8)

# print()

# v999 = V.Vertex('999')
# g2.add_vertex(v999)

# g2.bfs(self.v1,v999)
# print()
# g2.dfs(self.v1,v999)
# print()
# g2.dfs_recursive(self.v1,v999)
# print()


# g3 = Graph(vertices=[v1,v2,v3,v4,v5])

# g3.add_edge(src=v1, dest=v2, weight=10,directed=False)
# g3.add_edge(src=v1, dest=v3, weight=1,directed=False)
# g3.add_edge(src=v1, dest=v4, weight=10,directed=False)

# g3.add_edge(src=v2, dest=v5, weight=3,directed=False)

# g3.add_edge(src=v3, dest=v5, weight=15,directed=False)

# g3.add_edge(src=v4, dest=v3, weight=1,directed=False)

# w, path  = g3.shortest_path(v1,v2)

# g4 = Graph(vertices=[v1,v2,v3,v4,v5])

# g4.add_edge(src=v1, dest=v2, weight=11,directed=False)
# g4.add_edge(src=v1, dest=v3, weight=1,directed=False)
# g4.add_edge(src=v1, dest=v4, weight=12,directed=False)

# g4.add_edge(src=v2, dest=v5, weight=3,directed=False)

# g4.add_edge(src=v3, dest=v5, weight=15,directed=False)

# g4.add_edge(src=v4, dest=v3, weight=2,directed=False)

# w, path  = g4.shortest_path(v1,v2)

