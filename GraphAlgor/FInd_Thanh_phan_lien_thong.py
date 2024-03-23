# tim so thanh phan lien thong cua do thi
'''
Input:
7 6
1 2
1 3
2 3
5 6
6 7
5 7
Output:
3
'''
from collections import deque, defaultdict
class Graph:
    count_component = 0
    def __init__(self):
        self.adj = defaultdict(list)
    def addEdge(self,u,v):
        self.adj[u].append(v)
    visited = [False]*8
    def bfs(self,u):
        self.count_component += 1
        queue = []
        self.visited[u] = True
        queue.append(u)
        while queue:
            currentNode = queue.pop(0)
            print(currentNode,end = " ")
            for neibour in self.adj[currentNode]:
                if self.visited[neibour] == False:
                    self.visited[neibour] = True
                    queue.append(neibour)
    def findLienThong(self):
        for i in range(1,8):
            if self.visited[i] == False:
                self.bfs(i)
        print(self.count_component)
graph = Graph() 
graph.addEdge(7,6)
graph.addEdge(1,2)
graph.addEdge(1,3)
graph.addEdge(2,3)
graph.addEdge(5,6)
graph.addEdge(6,7)
graph.addEdge(5,7)
graph.findLienThong()
