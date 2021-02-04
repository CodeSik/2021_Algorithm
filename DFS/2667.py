from collections import deque
def bfs(x,y):
    queue = deque()
    global cnt
    global total_cnt
    graph[x][y] = total_cnt
    queue.append((x,y))
    visit[x][y] = True
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if nx<0 or nx >= N or ny <0 or ny>=N:
                continue

            if graph[nx][ny] == 1 and visit[nx][ny] == False and total_cnt==1 :
                queue.append((nx,ny))
                visit[nx][ny]=True
                cnt +=1
            elif graph[nx][ny] == 1 and visit[nx][ny] == False and total_cnt!=1 :
                graph[nx][ny]=total_cnt
                queue.append((nx,ny))
                visit[nx][ny]=True
                cnt +=1


    total_cnt+=1
    return
N = int(input())

graph = []
visit = [[False]*N for _ in range(N)]
for i in range(N):
    arr = list(map(int,input()))
    graph.append(arr)


# 상,하,좌,우
dx = [1,-1,0,0]
dy = [0,0,-1,1]
cnt_list = []
cnt = 1
total_cnt = 1
for i in range(N):
    for j in range(N):
        if graph[i][j] == 0:
            continue
        if graph[i][j] == 1 and visit[i][j] == False:
            bfs(i, j)
            cnt_list.append(cnt)
            cnt = 1


print(total_cnt-1)
cnt_list.sort()
for i in range(len(cnt_list)):
    print(cnt_list[i])
