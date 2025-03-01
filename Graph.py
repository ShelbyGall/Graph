#%%
import Vertex as v


class Graph:
    def __init__(self, vertices: list, edges: dict=None):
        self.vertices = vertices
        # TODO: immediately add the vertices as keys into the edges dictionary 
        if edges == None:
            self.edges = {}

    def add_edge(self, src: v, dest: v, weight: float=None, directed: bool=True):
        # check if there already is a edge added for the src vertex
        if self.edges.get(src):
            # if there is an edge, just append the new edge
            self.edges[src].append([dest, weight])
        else:
            # if there are no edges create list with the newly created edge
            self.edges[src] = [[dest, weight]]
        
        # if the edge isnt directed this means we need to add the edge both ways
        # repeat code block above
        if not directed:
            if self.edges.get(dest):
                self.edges[dest].append([src, weight])
            else:
                self.edges[dest] = [[src, weight]]

    def is_connected(self, src: v, dest: v):
        if self.edges.get(src) == None:
            return False
        
        for e in self.edges.get(src):
            if e[0] == dest:
                return True
            
        return False

    # TODO: BFS, DFS, Dijkstras

    def __str__(self) -> str:
        ret_str = ""
        temp = []
        for v in self.vertices:
            temp.append(f"{v.get_label()} -> ")
            if self.edges.get(v) != None:
                for e in self.edges.get(v):
                    temp.append(f"{e[0].get_label()} -> ")
            temp.append("\n")
        return ret_str.join(temp)
#%%

v1 = v.Vertex('1', {"branch name":"Scranton"})
v2 = v.Vertex('2')
v3 = v.Vertex('3')
v4 = v.Vertex('4')


vertices = [v1,v2,v3,v4]

#%%
print(v2)
print(v1)


#%%

my_graph = Graph(vertices=vertices)

# %%
my_graph.add_edge(src=v1, dest=v3, directed=False)
my_graph.add_edge(src=v3, dest=v2)
my_graph.add_edge(src=v4, dest=v1)

# %%
print(my_graph)
# %%
