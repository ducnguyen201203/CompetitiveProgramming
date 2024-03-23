# Using stack
from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.adj = defaultdict(list)
    def addEdge(self,u,v):
        self.adj[u].append(v)
    def dfs(self,u):
        visited = [False]*5
        stack = []
        visited[u] = True
        stack.append(u)
        while stack:
            currentNode = stack.pop(-1)
            print(currentNode)
            for neibour in self.adj[currentNode]:
                if visited[neibour] == False:
                    visited[neibour] = True
                    stack.append(neibour)
graph = Graph()
 
# Add edges to the graph
graph.addEdge(0, 1) # 0 - 1 - 2 
graph.addEdge(0, 2) # 1 - 3 - 4 
graph.addEdge(1, 3) # 2 - 4
graph.addEdge(1, 4)
graph.addEdge(2, 4)
graph.dfs(0)


# using recursion

from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.adj = defaultdict(list)
    def addEdge(self,u,v):
        self.adj[u].append(v)
    visited = [False]*5
    def dfs_recur(self,u):    
        self.visited[u] = True
        print(u,end=" ")
        for v in self.adj[u]:
            if self.visited[v] == False:
                self.dfs_recur(v)
    def dfs(self,u):
        visited = [False]*5
        stack = []
        visited[u] = True
        stack.append(u)
        while stack:
            currentNode = stack.pop(-1)
            print(currentNode)
            for neibour in self.adj[currentNode]:
                if visited[neibour] == False:
                    visited[neibour] = True
                    stack.append(neibour)
    
        
graph = Graph()
 
# Add edges to the graph
graph.addEdge(0, 1) # 0 - 1 - 2 
graph.addEdge(0, 2) # 1 - 3 - 4 
graph.addEdge(1, 3) # 2 - 4
graph.addEdge(1, 4)
graph.addEdge(2, 4)
graph.dfs_recur(0)
