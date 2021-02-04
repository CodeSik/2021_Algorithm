from collections import deque

def bfs(index_arr):
    queue = deque()

    tomato_cnt = 0
    after_tomato_cnt = 0
    cnt = 0
    days = 0
    for index in index_arr:
        queue.append(index)
        tomato_cnt+=1
    while queue:
        if tomato_cnt == 0:
            tomato_cnt = after_tomato_cnt
            after_tomato_cnt=0
            days+=1
        x, y = queue.popleft()
        cnt += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx == N or nx < 0 or ny == M or ny < 0:
                continue
            if graph[nx][ny] == -1:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = 1
                after_tomato_cnt += 1
                queue.append((nx, ny))
            if graph[nx][ny] == 1:
                continue
        tomato_cnt -= 1

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                return -1
    return days


M,N = map(int,input().split())
#N이 세로, M이 가로
graph = []
for i in range(N):
    arr = list(map(int,input().split()))
    graph.append(arr)

#상, 하, 좌, 우
dx = [1,-1,0,0]
dy = [0,0,-1,1]

index_arr = []
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            index_arr.append((i,j))
print(bfs(index_arr))


