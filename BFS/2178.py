from collections import deque
def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx == N or nx <0 or ny == M or ny <0:
                continue

            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y]+1
                queue.append((nx,ny))
    return graph[N-1][M-1]




N,M = map(int,input().split())
graph = []
for i in range(N):
    arr = list(map(int,input()))
    graph.append(arr)

#상, 하, 좌, 우
dx = [1,-1,0,0]
dy = [0,0,-1,1]

print(bfs(0,0))

