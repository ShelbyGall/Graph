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
        v1 = V.Vertex('1')
        v2 = V.Vertex('2')
        v3 = V.Vertex('3')
        v4 = V.Vertex('4')
        v5 = V.Vertex('5')
        v6 = V.Vertex('6')
        v7 = V.Vertex('7')
        v8 = V.Vertex('8')
        v999 = V.Vertex('999')

        vertices = [v1,
                        v2,
                        v3,
                        v4]
        no_edge_graph = G.Graph(vertices=vertices)

        pop_edge_graph = G.Graph(vertices=vertices)

        pop_edge_graph.add_edge(src=v1, dest=v3, directed=False)
        pop_edge_graph.add_edge(src=v3, dest=v2)
        pop_edge_graph.add_edge(src=v4, dest=v1)
        pop_edge_graph.add_edge(src=v1, dest=v3, directed=False)
        pop_edge_graph.add_edge(src=v3, dest=v2)
        pop_edge_graph.add_edge(src=v4, dest=v1)

        vertices2 = [v1,v2,v3,v4,v5,v6,v7,v8]
        g2 = G.Graph(vertices=vertices2)

        g2.add_edge(src=v1, dest=v2, directed=False)
        g2.add_edge(src=v1, dest=v3, directed=False)
        g2.add_edge(src=v1, dest=v4, directed=False)
        g2.add_edge(src=v3, dest=v6, directed=False)
        g2.add_edge(src=v3, dest=v7, directed=False)
        g2.add_edge(src=v4, dest=v7, directed=False)
        g2.add_edge(src=v6, dest=v8, directed=False)

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

        self.g2.add_vertex(self.v999)
        self.g2.bfs(self.v1,self.v999)

        self.g2.delete_vertex(self.v999)

    def test_dfs(self):
        self.g2.dfs(self.v1,self.v8)

        self.g2.add_vertex(self.v999)
        self.g2.dfs(self.v1,self.v999)


        self.g2.delete_vertex(self.v999)

    def test_dfs_recursive(self):
        self.g2.dfs_recursive(self.v1, self.v8) 
        self.g2.dfs_recursive(self.v1,self.v999)


# %%
v1 = V.Vertex('1')
v2 = V.Vertex('2')
v3 = V.Vertex('3')
v4 = V.Vertex('4')
v5 = V.Vertex('5')
v6 = V.Vertex('6')
v7 = V.Vertex('7')
v8 = V.Vertex('8')
v999 = V.Vertex('999')
vertices2 = [v1,v2,v3,v4,v5,v6,v7,v8]
g2 = G.Graph(vertices=vertices2)

g2.add_edge(src=v1, dest=v2, directed=False)
g2.add_edge(src=v1, dest=v3, directed=False)
g2.add_edge(src=v1, dest=v4, directed=False)
g2.add_edge(src=v3, dest=v6, directed=False)
g2.add_edge(src=v3, dest=v7, directed=False)
g2.add_edge(src=v4, dest=v7, directed=False)
g2.add_edge(src=v6, dest=v8, directed=False)

g2.bfs(v1,v8)


# g3 = G.Graph(vertices=[v1,v2,v3,v4,v5])

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

