ans = 0
def dfs(x,y):
    if x <= -1 or x>= N or y<=-1 or y>= M:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x-1,y)
        dfs(x + 1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False


N,M = map(int,input().split())

graph = []
visit = [False]*N*M
for i in range(N):
    line = list(map(int,input()))
    graph.append(line)

for i in range(N):
    for j in range(M):
        if dfs(i,j) == True:
            ans+=1
print(ans)