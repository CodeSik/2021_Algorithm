ans = 0
def dfs(s):
    visit_dfs[s] = True
    global ans
    ans +=1
    for i in graph[s]:
        if not visit_dfs[i]:
            dfs(i)



N = int(input())
M = int(input())
graph = [[]*(N+1) for _ in range(N+1)]
visit_dfs=[False]*(N+1)
for i in range(M):
    arr = list(map(int,input().split()))
    graph[arr[0]].append(arr[1])
    graph[arr[1]].append(arr[0])
    graph[arr[0]].sort()

dfs(1)
print(ans-1)
