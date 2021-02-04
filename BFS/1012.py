from collections import deque
def bfs(x,y):
    global cnt
    queue = deque()
    queue.append((x,y))

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx == N or nx <0 or ny == M or ny <0:
                continue

            if graph[nx][ny] == 1 and visit[nx][ny] == False:
                queue.append((nx,ny))
                visit[nx][ny] = True
    cnt+=1
    return





T = int(input())
'''
M: 가로 길이
N: 세로 길이
K: 배축 심어져 있는 위치의 갯수
'''
cnt = 0
# 상,하,좌,우
dx = [1,-1,0,0]
dy = [0,0,-1,1]

for _ in range(T):
    cnt = 0
    M,N,K = map(int,input().split())

    #M*N의 그래프
    graph = [[0]*M for _ in range(N)]
    visit = [[False] * M for _ in range(N)]
    for i in range(K):
        x,y = map(int,input().split())
        graph[y][x] = 1

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                continue
            if graph[i][j] == 1 and visit[i][j] == False:
                bfs(i,j)

    print(cnt)


