'''
자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
고른 수열은 오름차순이어야 한다.
'''
#12:22

def func(k):
    if k == M:
        copy_arr = result.copy()
        copy_arr.sort()
        isSame = True
        for i in range(M):
            if copy_arr[i] != result[i]:
                isSame = False
        if isSame:
            for num in result:
                print(num,end=' ')
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


