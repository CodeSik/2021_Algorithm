'''
1. 처음 출발할 때 기름을 넣고 출발해야 한다.
2. 기름통의 크기는 무제한
3. 연비는 1L
4. 도시에는 하나의 주유소가 있으며 리터당 가격은 다르다.
--> 제일 왼쪽 도시에서 제일 오른쪽으로 갈 때 최소의 비용을 구하는 문제

입력
4
2 3 1
5 2 4 1

1. 도시의 갯수
2. 도로 사이의 거리값
3. 각 도시의 리터당 가격
'''

#입력
n = int(input())
weight = list(map(int,input().split()))
price = list(map(int,input().split()))

min = price[0]
ans = 0
for i in range(n-1):
    if min > price[i]:
        min = price[i]
    ans += min*weight[i]
print(ans)