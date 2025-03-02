#%%
import Vertex as v
from collections import deque


class Graph:


    def __init__(self, vertices: list, edges: dict=None):
        self.vertices = vertices
        if edges == None:
            self.edges = {}
            # if no edges were passed into the constructor, 
            # populate the edges to be the empty lists meaning
            # no vertices are connected in the graph
            for v in self.vertices:
                self.edges[v] = []
        else:
            self.edges = edges
    

    def add_vertex(self, vertex: v) -> None:
        # if the vertex isn't already in the graph then add the vertex
        # to both the vertices list and the edges dict
        if self.edges.get(vertex) == None:
            self.vertices.append(vertex)
            self.edges[vertex] = []


    def add_edge(self, src: v, dest: v, weight: float=None, directed: bool=True) -> None:
        # if either the src or dest vertices arent in the graph, dont add the edge
        if (self.edges.get(src) == None) or (self.edges.get(dest) == None):
            print("Error: Vertex not in graph")
            return 
        
        # if the src and dest vertices aren't already connected, add the edge
        if not self.is_connected(src, dest):
            # add new edge
            self.edges[src].append([dest, weight])
            
            # if the edge isnt directed this means we need to add the edge both ways
            if not directed:
                # if the src and dest vertices aren't already connected, add the edge
                if not self.is_connected(dest, src):
                    self.edges[dest].append([src, weight])


    def is_connected(self, src: v, dest: v) -> bool:
        # get the list of edges in the dict at the src key
        # iterate through that list and check if any of the 
        # adjacent vertices in the list are the dest vertex
        for e in self.edges.get(src):
            if e[0] == dest:
                return True
            
        return False


    
    def bfs(self, src: v, dest: v) -> None:
        # visited set to keep track of vertices we've already visited
        visited: set = set()
        # queue used for exploring adjacent vertices
        queue: deque = deque()

        # add the src vertex to the queue 
        queue.append(src)
        # keep checking the queue to see if its empty
        # if the queue is empty; searching is complete
        # and the search was unsuccessful
        while len(queue) != 0:
            # grab the current vertex from the queue
            curr_ver = queue.popleft()

            # if the current vertex has already been visited then go to next
            # iteration
            if curr_ver in visited:
                continue
            
            # if the current vertex hasnt been visited, then add it 
            # to the visited vertex to show we are visiting it
            visited.add(curr_ver)

            # "visit" the current vertex
            print(curr_ver)

            # if the current vertex is what we are searching for then 
            # return and the search is successful
            if curr_ver == dest:
                print("found")
                return

            # if current vertex isnt what we are searching for then
            # add all adjacent vertices of the current vertex to the 
            # exploration queue as long as the adjacent vertex hasnt 
            # already been visited
            for adj_ver in self.edges.get(curr_ver):
                if adj_ver[0] not in visited:
                    queue.append(adj_ver[0])
        
        # search was unsuccessful
        print(f"{dest} cannot be found from {src}")
    

    def dfs(self, src: v, dest: v) -> None:
        # visited set to keep track of vertices we've already visited
        visited: set = set()
        # stack used for exploring adjacent vertices
        stack: deque = deque()

        # add the src vertex to the stack
        stack.append(src)
        # keep checking the stack to see if its empty
        # if the stack is empty; searching is complete
        # and the search was unsuccessful
        while len(stack) != 0:
            # grab the current vertex from the stack
            curr_ver = stack.pop()

            # if the current vertex has already been visited then go to next
            # iteration
            if curr_ver in visited:
                continue

            # if the current vertex hasnt been visited, then add it 
            # to the visited vertex to show we are visiting it
            visited.add(curr_ver)

            # "visit" the current vertex
            print(curr_ver)

            # if the current vertex is what we are searching for then 
            # return and the search is successful
            if curr_ver == dest:
                print("found")
                return

            # if current vertex isnt what we are searching for then
            # add all adjacent vertices of the current vertex to the 
            # exploration stack as long as the adjacent vertex hasnt 
            # already been visited
            for adj_ver in self.edges.get(curr_ver):
                if adj_ver[0] not in visited:
                    stack.append(adj_ver[0])
        
        # search was unsuccessful
        print(f"{dest} cannot be found from {src}")


    def dfs_recursive(self, src: v, dest: v) -> None:
        # visited set to keep track of vertices we've already visited
        visited: set = set()
        # call helper recursive funciton with the visited set as a parameter
        found = self.__dfs_recur_helper__(src, dest, visited)
        # if the recursive function doesnt return True then the dest vertex was not found
        if not found:
            print(f"{dest} cannot be found from {src}")

    def __dfs_recur_helper__(self, src: v, dest: v, visited: set):
        # if the current vertex has already been visited go to next function call
        if src in visited:
            return
        
        # if the current vertex hasnt been visited, then add it 
        # to the visited vertex to show we are visiting it
        visited.add(src)

        # "visit" the current vertex
        print(src)

        # if the current vertex is what we are searching for then 
        # return and the search is successful
        if src == dest:
            print("found")
            return True
        
        # if current vertex isnt what we are searching for then
        # recursively perform dfs on all adjacent vertices 
        for adj_ver in self.edges.get(src):
            if adj_ver[0] not in visited:
                found = self.__dfs_recur_helper__(adj_ver[0], dest, visited)
                # if the vertex has been found from the recursive funciton call
                # then return True denoting that the dest vertex has been found
                if found: 
                    return True


    # TODO: Dijkstras, MST, Disjoint sets, topological sort

    def __str__(self) -> str:
        ret_str: str = ""
        temp: list = []
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
v5 = v.Vertex('5')
v6 = v.Vertex('6')
v7 = v.Vertex('7')
v8 = v.Vertex('8')

print(v1)
print(v2)

vertices = [v1,v2,v3,v4]

my_graph = Graph(vertices=vertices)

my_graph.add_edge(src=v1, dest=v3, directed=False)
my_graph.add_edge(src=v3, dest=v2)
my_graph.add_edge(src=v4, dest=v1)

my_graph.add_edge(src=v5, dest=v2)

print(my_graph)

# %%
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


# %%
v999 = v.Vertex('999')
g2.add_vertex(v999)

g2.bfs(v1,v999)
print()
g2.dfs(v1,v999)
print()
g2.dfs_recursive(v1,v999)
print()
# %%
