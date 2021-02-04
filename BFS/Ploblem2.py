from collections import deque
ans = -1

N,M = map(int,input().split())
graph = []
for i in range(N):
    graph.append(list(map(int,input())))

#상, 하, 좌, 우
dx = [-1, 1, 0 ,0]
dy = [0,0,-1,1]


def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx =x + dx[i]
            ny =y + dy[i]
            if nx<0 or nx >= N or ny <0 or ny>=M:
                continue



wallCount = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == 2 and wallCount < 3:
            result = bfs(i,j)
            if(ans < result):
                ans = result