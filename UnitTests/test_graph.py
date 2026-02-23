# %%
import sys
sys.path.append('./')

import unittest

import Vertex as V
from Graph import Graph


# TODO: Turn all these code blocks below into unit tests 
class TestGraph(unittest.TestCase):
    v1 = V.Vertex('1')
    v2 = V.Vertex('2')
    v3 = V.Vertex('3')
    v4 = V.Vertex('4')
    v5 = V.Vertex('5')
    v6 = V.Vertex('6')
    v7 = V.Vertex('7')
    v8 = V.Vertex('8')

    vertices = [v1,v2,v3,v4]

    my_graph = Graph(vertices=vertices)

    my_graph.add_edge(src=v1, dest=v3, directed=False)
    my_graph.add_edge(src=v3, dest=v2)
    my_graph.add_edge(src=v4, dest=v1)

    my_graph.add_edge(src=v5, dest=v2)


#%% test 1




#%% test 2


my_graph.add_edge(src=v1, dest=v3, directed=False)
my_graph.add_edge(src=v3, dest=v2)
my_graph.add_edge(src=v4, dest=v1)

my_graph.add_edge(src=v5, dest=v2)

print(my_graph)

vertices2 = [v1,v2,v3,v4,v5,v6,v7,v8]
g2 = Graph(vertices=vertices2)

g2.add_edge(src=v1, dest=v2, directed=False)
g2.add_edge(src=v1, dest=v3, directed=False)
g2.add_edge(src=v1, dest=v4, directed=False)

g2.add_edge(src=v3, dest=v6, directed=False)
g2.add_edge(src=v3, dest=v7, directed=False)
g2.add_edge(src=v4, dest=v7, directed=False)

g2.add_edge(src=v6, dest=v8, directed=False)

g2.bfs(v1,v8)
print()
g2.dfs(v1,v8)
print()
g2.dfs_recursive(v1,v8)
print()

v999 = V.Vertex('999')
g2.add_vertex(v999)

g2.bfs(v1,v999)
print()
g2.dfs(v1,v999)
print()
g2.dfs_recursive(v1,v999)
print()
# %% test 3

g3 = Graph(vertices=[v1,v2,v3,v4,v5])

g3.add_edge(src=v1, dest=v2, weight=10,directed=False)
g3.add_edge(src=v1, dest=v3, weight=1,directed=False)
g3.add_edge(src=v1, dest=v4, weight=10,directed=False)

g3.add_edge(src=v2, dest=v5, weight=3,directed=False)

g3.add_edge(src=v3, dest=v5, weight=15,directed=False)

g3.add_edge(src=v4, dest=v3, weight=1,directed=False)

w, path  = g3.shortest_path(v1,v2)
# %% test 4
g4 = Graph(vertices=[v1,v2,v3,v4,v5])

g4.add_edge(src=v1, dest=v2, weight=11,directed=False)
g4.add_edge(src=v1, dest=v3, weight=1,directed=False)
g4.add_edge(src=v1, dest=v4, weight=12,directed=False)

g4.add_edge(src=v2, dest=v5, weight=3,directed=False)

g4.add_edge(src=v3, dest=v5, weight=15,directed=False)

g4.add_edge(src=v4, dest=v3, weight=2,directed=False)

w, path  = g4.shortest_path(v1,v2)

# %% test 5
