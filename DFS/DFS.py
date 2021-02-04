def dfs(s,graph,v):
    v[s] = True
    print(s, end='')
    for i in graph[s]:
        if not v[i]:
            dfs(i,graph,v)


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

dfs(1,graph,v)
