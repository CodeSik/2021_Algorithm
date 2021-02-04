from collections import deque

def dfs(s):
    visit_dfs[s] = True
    print(s,end=' ')
    for i in graph[s]:
        if not visit_dfs[i]:
            dfs(i)

def bfs(s):
    queue = deque()
    queue.append(s)
    visit_bfs[s]=True

    while queue:
        n = queue.popleft()
        print(n,end=' ')
        for i in graph[n]:
            if not visit_bfs[i]:
                queue.append(i)
                visit_bfs[i]=True
    return



N, M, V = map(int,input().split())

visit_dfs=[False]*(N+1)
visit_bfs=[False]*(N+1)
#중요
graph = [[]*(N+1) for _ in range(N+1)]

for _ in range(M):
    arr = list(map(int,input().split()))
    graph[arr[0]].append(arr[1])
    graph[arr[1]].append(arr[0])
    graph[arr[0]].sort()

print(graph)
dfs(V)
print()
bfs(V)

