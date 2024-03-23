# cai dat bfs
from collections import defaultdict, deque
 
class Graph:
    def __init__(self):
        self.adj = defaultdict(list)
    
    def addEdge(self,u,v):
        self.adj[u].append(v)
    def bfs(self,u):
        visited = [False]*5
        queue = []
        visited[u] = True
        queue.append(u)
        while queue:
            currentnode = queue.pop(0)
            print(currentnode, end = " ")
            for v in self.adj[currentnode]:
                if visited[v] == False:
                    visited[v] = True
                    queue.append(v)
        
graph = Graph()
 
# Add edges to the graph
graph.addEdge(0, 1)
graph.addEdge(0, 2)
graph.addEdge(1, 3)
graph.addEdge(1, 4)
graph.addEdge(2, 4)
graph.bfs(0)
