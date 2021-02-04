from collections import deque
tmp_queue = deque()
visit = deque()
for i in range(100001):
    visit.append(0)
def bfs(N,K):
    queue = deque()
    dx = [-1,1,2]
    queue.append(N)
    cnt = 0
    if N == K:
        return cnt

    while queue:
        while queue:
            tmp_queue.append(queue.popleft())
        cnt+=1

        while tmp_queue:
            x = tmp_queue.popleft()
            for i in range(3):
                if i == 2:
                    nx = x * dx[i]
                else:
                    nx = x + dx[i]
                if 0<=nx<=100000:
                    visit[nx] +=1
                if nx <0 or nx > 100000:
                    continue
                if nx !=K and visit[nx] == 1:
                    queue.append(nx)
                elif nx == K:
                    return cnt

N,K = map(int,input().split())
result = bfs(N,K)
print(result)
