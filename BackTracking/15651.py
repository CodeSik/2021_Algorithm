'''
자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

1부터 N까지 자연수 중에서 M개를 고른 수열
같은 수를 여러 번 골라도 된다.
'''

#12;29

def func(k):
    if k == M:
        for num in result:
            print(num,end=' ')
        print('')

    else:
        for i in range(len(arr)):
            result[k] = arr[i]
            func(k+1)



N,M = map(int,input().split())

arr = [i+1 for i in range(N)]
result = [0 for i in range(M)]
# visit = [False for i in range(N)]
func(0)