# thuat toan loang
'''
De bai: cho ma tran 
[[1,1,1,0,0],
[1,1,0,0,1],
[0,0,0,1,1],
[1,0,0,0,0],
[0,1,1,1,0]]
Công việc của bạn là đếm số lượng vết loang trên biển và kích thước tương ứng của từng vết.
output: {5,3,1,3}
'''
from collections import deque, defaultdict
maxN = 300
n,m = 0,0

visit = [[False]*(maxN + 1) for _ in range(maxN+1)]
slick = []
moveX = [0,0,1,-1]
moveY = [1,-1,0,0]
def bfs(sx, sy):
    sizeslick = 1
    q = deque([(sx,sy)])
    visit[sx][sy] = True
    while q:
        x,y = q.popleft()
        for i in range(4):
            u = x+moveX[i]
            v = y+moveY[i]
            if u > 4 or u < 0:
                continue
            if v > 4 or v < 0:
                continue
            if beach[u][v] and not visit[u][v]:
                sizeslick += 1
                visit[u][v] = True
                q.append((u,v))
    return sizeslick 
beach = [[1,1,1,0,0],
[1,1,0,0,1],
[0,0,0,1,1],
[1,0,0,0,0],
[0,1,1,1,0]]
for i in range(5):
    for j in range(5):
        if beach[i][j] and not visit[i][j]:
            slick.append(bfs(i,j))
print(slick)
