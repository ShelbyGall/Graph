#%%
import Vertex as v
from collections import deque
import heapq
from DisjointSet import DisjointSet



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


    def delete_vertex(self, vertex: v) -> None:
        # check if the vertex is in the graph
        if self.edges.get(vertex):

            # remove vertex from vertices list
            self.vertices.remove(vertex)

            # check all vertices edge list for the vertex to be deleted
            for e in self.edges.keys():
                # dont need to perform delete_edge on the vertex to be deleted
                # in the edges dict as it will be wasted time
                if e != vertex:
                    # delete the edge between current edge and the vertex to be deleted
                    self.delete_edge(e, vertex)

            # remove vertex from edges dict
            self.edges.pop(vertex)


    def add_edge(self, src: v, dest: v, weight: float=None, directed: bool=True) -> None:
        # if either the src or dest vertices arent in the graph, dont add the edge
        if (self.edges.get(src) == None) or (self.edges.get(dest) == None):
            print("Error: Vertex not in graph")
            return 
        
        # if the src and dest vertices aren't already connected, add the edge
        if not self.is_connected(src, dest):
            # add new edge
            self.edges[src].append([src, dest, weight])
            
            # if the edge isnt directed this means we need to add the edge both ways
            if not directed:
                # if the src and dest vertices aren't already connected, add the edge
                if not self.is_connected(dest, src):
                    self.edges[dest].append([dest, src, weight])

    
    def delete_edge(self, src: v, dest: v) -> None:
        # check if the src and dest vertices exist in the graph and if they are connected
        if self.edges.get(src) and self.edges.get(dest) and self.is_connected(src, dest):
            # get the src list of edges
            curr_edges: list = self.edges.get(src)
            # iterate over src edge list to find the correct edge
            for e in curr_edges:
                if e[0] == src and e[1] == dest:
                    curr_edges.remove(e)
            
        


    def get_edges(self) -> list:
        all_edges = []
        # iterate though all vertices
        for k in self.edges.keys():
            # iterate though the current vertex's adjacent edges
            for e in self.edges.get(k):
                # add it to a list
                all_edges.append(e)
        return all_edges


    def is_connected(self, src: v, dest: v) -> bool:
        # get the list of edges in the dict at the src key
        # iterate through that list and check if any of the 
        # adjacent vertices in the list are the dest vertex
        for e in self.edges.get(src):
            if e[1] == dest:
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
                if adj_ver[1] not in visited:
                    queue.append(adj_ver[1])
        
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
                if adj_ver[1] not in visited:
                    stack.append(adj_ver[1])
        
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
            if adj_ver[1] not in visited:
                found = self.__dfs_recur_helper__(adj_ver[1], dest, visited)
                # if the vertex has been found from the recursive funciton call
                # then return True denoting that the dest vertex has been found
                if found: 
                    return True


    def shortest_path(self, src: v, dest: v) -> tuple[int, list]:

        # dict to keep track of the vertices that connect to each other
        # on the shortest path from src to dest
        v_to: dict = dict(zip(self.vertices, [None]*len(self.vertices)))

        # dict to keep track of the shortest weights to each vertex
        w_to: dict = dict(zip(self.vertices, [None]*len(self.vertices)))

        w_to.update({src:0})
        # visited set to keep track of vertices we've already visited
        visited: set = set()
        # use a priority queue/heap for exploring adjacent vertices
        queue: list = []

        # due to heapq restrictions of tuple comparisons when the
        # two tuples have the same priority(weight) but with non-comparable tasks(Vertex)
        # we can store a counter as the second value in the tuple which will count up 
        # every time a edge is passed into the priority queue and when two edges of equal weights 
        # are compared, the tuple comparison will compare the counts which will never be the same
        #  Before: (weight, vertex)             if weights are equal then it attempts to compare vertex(cant be done)
        #  After: (weight, count, vertex)       if weights are equal then it compares count
        count = 0

        # add the src vertex to the queue 
        heapq.heappush(queue, (0, count, src))

        # keep checking the queue to see if its empty
        # if the queue is empty; searching is complete
        # and the search was unsuccessful
        while len(queue) != 0:
            print('here')
            # grab the current vertex from the queue
            _, _, curr_ver = heapq.heappop(queue)

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
                # returns a tuple generated from the variables populated in this funciton
                # and are gives as (weight of shortest path between src and dest, vertices along the shortest path)
                return self.__short_path_return__(src=src, dest=dest,v_to=v_to,w_to=w_to)

            # if current vertex isnt what we are searching for then
            # add all adjacent vertices of the current vertex to the 
            # exploration queue as long as the adjacent vertex hasnt 
            # already been visited
            for adj_ver in self.edges.get(curr_ver):
                if adj_ver[1] not in visited:
                    # increment the counter to allow the comparison of equal weights in the heapq(priority queue)
                    count += 1
                    heapq.heappush(queue, (adj_ver[2], count, adj_ver[1]))

                    # if there is no shortest weight recorded in w_to for the adjacent vertex
                    # or the newly discovered paths weight is smaller than the weight recorded in w_to for the adjacent vertex
                    if (w_to.get(adj_ver[1]) == None) or (w_to.get(adj_ver[1]) > adj_ver[2] + w_to.get(curr_ver)):
                        # update the w_to and v_to with the newly discovered path
                        w_to.update({adj_ver[1]:adj_ver[2] + w_to.get(curr_ver)})
                        v_to.update({adj_ver[1]: curr_ver})

        
    def __short_path_return__(self, src:v, dest: v, v_to: dict, w_to: dict) -> tuple[int, list]:
        # return the list of vertices along the shortest path
        # from src to dest and the weight it took to get there
        path = []
        path.append(dest)
        c = v_to.get(dest)
        
        while True:
            path.append(c)
            if c == src:
                return (w_to.get(dest), path[::-1])
            c = v_to.get(c)




    def kruskals_mst(self) -> tuple[int, list]:
        # create the disjoint set to account for cycles/connectivity
        ds = DisjointSet(self.vertices)
        
        # get all edges in the graph
        all_edges = self.get_edges()

        # sort our edges by their weight
        sorted_edges = sorted(all_edges, key=lambda e: e[2])

        # init the cost of the current mst
        cost: int = 0

        # init our list of edges picked
        edges_picked: list = []
        
        # iterate over our sorted edges
        for edge in sorted_edges:
            # find the disjoint set "representatives"(root) of the vertices in our current edge
            par1 = ds.find(edge[0])
            par2 = ds.find(edge[1])

            # if the current edge being looked at doesnt create a cycle,
            # chose the edge, update the cost and connect them in the disjoint set
            if par1 != par2:
                edges_picked.append(edge)
                cost += edge[2]
                ds.union(edge[0], edge[1])
            
            # if we have chosen V - 1 edges then our MST will be complete
            if len(edges_picked) == len(self.vertices) - 1:
                return (cost, edges_picked)


    # TODO: Disjoint sets OPTIMIZATION, prims mst???, topological sort, APPLICATION, 

    def __str__(self) -> str:
        ret_str: str = ""
        temp: list = []
        for v in self.vertices:
            temp.append(f"{v.get_label()} -> ")
            if self.edges.get(v) != None:
                for e in self.edges.get(v):
                    temp.append(f"{e[1].get_label()} -> ")
            temp.append("\n")
        return ret_str.join(temp)
    
    def __repr__(self) -> str:
        return f"graph: {self.vertices}"



    

#%%

v1 = v.Vertex('1')
v2 = v.Vertex('2')
v3 = v.Vertex('3')
v4 = v.Vertex('4')
v5 = v.Vertex('5')
v6 = v.Vertex('6')
v7 = v.Vertex('7')
v8 = v.Vertex('8')

print(v1)
print(v2)
#%%
vertices = [v1,v2,v3,v4]

my_graph = Graph(vertices=vertices)

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

v999 = v.Vertex('999')
g2.add_vertex(v999)

g2.bfs(v1,v999)
print()
g2.dfs(v1,v999)
print()
g2.dfs_recursive(v1,v999)
print()
# %%

g3 = Graph(vertices=[v1,v2,v3,v4,v5])

g3.add_edge(src=v1, dest=v2, weight=10,directed=False)
g3.add_edge(src=v1, dest=v3, weight=1,directed=False)
g3.add_edge(src=v1, dest=v4, weight=10,directed=False)

g3.add_edge(src=v2, dest=v5, weight=3,directed=False)

g3.add_edge(src=v3, dest=v5, weight=15,directed=False)

g3.add_edge(src=v4, dest=v3, weight=1,directed=False)

w, path  = g3.shortest_path(v1,v2)
# %%
g4 = Graph(vertices=[v1,v2,v3,v4,v5])

g4.add_edge(src=v1, dest=v2, weight=11,directed=False)
g4.add_edge(src=v1, dest=v3, weight=1,directed=False)
g4.add_edge(src=v1, dest=v4, weight=12,directed=False)

g4.add_edge(src=v2, dest=v5, weight=3,directed=False)

g4.add_edge(src=v3, dest=v5, weight=15,directed=False)

g4.add_edge(src=v4, dest=v3, weight=2,directed=False)

w, path  = g4.shortest_path(v1,v2)

# %%
