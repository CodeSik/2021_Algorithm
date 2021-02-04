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
        x, y, z= queue.popleft()
        cnt += 1
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            # print(nx,ny,nz)
            # print(N,M,H)
            if nx == N or nx < 0 or ny == M or ny < 0 or nz == H or nz <0:
                continue
            if graph[nz][nx][ny] == -1:
                continue
            if graph[nz][nx][ny] == 0:
                graph[nz][nx][ny] = 1
                after_tomato_cnt += 1
                queue.append((nx, ny,nz))
            if graph[nz][nx][ny] == 1:
                continue
        tomato_cnt -= 1

    for i in range(H):
        for j in range(N):
            for k in range(M):
                if graph[i][j][k] == 0:
                    return -1
    return days


M,N,H = map(int,input().split())
#N이 세로, M이 가로, H는 높이
graph = []
sub_graph = []
for i in range(H):
    for j in range(N):
        arr = list(map(int,input().split()))
        sub_graph.append(arr)
    graph.append(sub_graph)
    sub_graph=[]

# for i in range(H):
#     print(f"Height {i}")
#     for j in range(N):
#         print(graph[i][j])
#상, 하, 좌, 우, 위, 아
dx = [1,-1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,1,-1]
index_arr = []
for i in range(H):
    for j in range(N):
        for k in range(M):
            if graph[i][j][k] == 1:
                index_arr.append((j,k,i))
# print(index_arr)
print(bfs(index_arr))



