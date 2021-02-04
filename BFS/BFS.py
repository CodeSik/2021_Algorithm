from collections import deque

def bfs(s,graph,v):
    queue = deque()
    queue.append(s)
    v[s] = True
    while queue:
        s = queue.popleft()
        print(s,end='')
        for i in graph[s]:
            if not v[i]:
                queue.append(i)
                v[i]=True
graph =[
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

v = [False]*9

bfs(1,graph,v)