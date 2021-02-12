def func(k):
    if k == M:
        for num in result:
            print(num,end=" ")
        print('')
    else:
        for i in range(len(arr)):
            if not visit[i]:
                result[k] = arr[i]
                visit[i] = True
                func(k+1)
                visit[i] = False



N,M = map(int,input().split())
arr = [i+1 for i in range(N)]
result = [0 for i in range(M)]
visit = [False for i in range(N)]
func(0)