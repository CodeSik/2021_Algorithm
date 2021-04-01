from itertools import permutations
N,M = map(int,input().split())
num_list = list(map(int,input().split()))

per_list = list(permutations(num_list,3))

differ = M
ans = -1
for per in per_list:
    temp = M - sum(per)
    if temp < differ and temp >= 0:
        differ = temp
        ans = sum(per)
print(ans)