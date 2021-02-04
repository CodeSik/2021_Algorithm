'''
로봇 청소기가 주어졌을 때, 청소하는 영역의 개수를 구하는 프로그램을 작성하시오.

로봇 청소기가 있는 장소는 N×M 크기의 직사각형으로 나타낼 수 있으며, 1×1크기의 정사각형 칸으로 나누어져 있다. 각각의 칸은 벽 또는 빈 칸이다. 청소기는 바라보는 방향이 있으며,
이 방향은 동, 서, 남, 북중 하나이다. 지도의 각 칸은 (r, c)로 나타낼 수 있고, r은 북쪽으로부터 떨어진 칸의 개수, c는 서쪽으로 부터 떨어진 칸의 개수이다.

로봇 청소기는 다음과 같이 작동한다.

1. 현재 위치를 청소한다.
2. 현재 위치에서 현재 방향을 기준으로 왼쪽방향부터 차례대로 탐색을 진행한다.
    1) 왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면, 그 방향으로 회전한 다음 한 칸을 전진하고 1번부터 진행한다.
    2) 왼쪽 방향에 청소할 공간이 없다면, 그 방향으로 회전하고 2번으로 돌아간다.
    3) 네 방향 모두 청소가 이미 되어있거나 벽인 경우에는, 바라보는 방향을 유지한 채로 한 칸 후진을 하고 2번으로 돌아간다.
    4) 네 방향 모두 청소가 이미 되어있거나 벽이면서, 뒤쪽 방향이 벽이라 후진도 할 수 없는 경우에는 작동을 멈춘다.
로봇 청소기는 이미 청소되어있는 칸을 또 청소하지 않으며, 벽을 통과할 수 없다.

입력
첫째 줄에 세로 크기 N과 가로 크기 M이 주어진다. (3 ≤ N, M ≤ 50)

둘째 줄에 로봇 청소기가 있는 칸의 좌표 (r, c)와 바라보는 방향 d가 주어진다. d가 0인 경우에는 북쪽을, 1인 경우에는 동쪽을, 2인 경우에는 남쪽을, 3인 경우에는 서쪽을 바라보고 있는 것이다.

셋째 줄부터 N개의 줄에 장소의 상태가 북쪽부터 남쪽 순서대로, 각 줄은 서쪽부터 동쪽 순서대로 주어진다. 빈 칸은 0, 벽은 1로 주어진다. 지도의 첫 행, 마지막 행, 첫 열, 마지막 열에 있는 모든 칸은 벽이다.

로봇 청소기가 있는 칸의 상태는 항상 빈 칸이다.

출력
로봇 청소기가 청소하는 칸의 개수를 출력한다.

3 3
1 1 0
1 1 1
1 0 1
1 1 1

1

11 10
7 4 0
1 1 1 1 1 1 1 1 1 1
1 0 0 0 0 0 0 0 0 1
1 0 0 0 1 1 1 1 0 1
1 0 0 1 1 0 0 0 0 1
1 0 1 1 0 0 0 0 0 1
1 0 0 0 0 0 0 0 0 1
1 0 0 0 0 0 0 1 0 1
1 0 0 0 0 0 1 1 0 1
1 0 0 0 0 0 1 1 0 1
1 0 0 0 0 0 0 0 0 1
1 1 1 1 1 1 1 1 1 1

57
'''


def moveDirLeft(d):
    if(d == 0):
        d = 3
    else:
        d -= 1
    return d


def move(x,y,dir):
    nx = x + dx[dir]
    ny = y + dy[dir]
    return nx,ny

N, M = map(int,input().split())
x,y,d = map(int,input().split())
arr = [[0]*M for _ in range(N)]
for i in range(N):
    inputList = list(map(int, input().split()))
    for j in range(M):
        arr[i][j] = inputList[j]

'''
1. 현재 위치를 청소한다.
2. 현재 위치에서 현재 방향을 기준으로 왼쪽방향부터 차례대로 탐색을 진행한다.
    1) 왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면, 그 방향으로 회전한 다음 한 칸을 전진하고 1번부터 진행한다.
    2) 왼쪽 방향에 청소할 공간이 없다면, 그 방향으로 회전하고 2번으로 돌아간다.
    3) 네 방향 모두 청소가 이미 되어있거나 벽인 경우에는, 바라보는 방향을 유지한 채로 한 칸 후진을 하고 2번으로 돌아간다.
    4) 네 방향 모두 청소가 이미 되어있거나 벽이면서, 뒤쪽 방향이 벽이라 후진도 할 수 없는 경우에는 작동을 멈춘다.
로봇 청소기는 이미 청소되어있는 칸을 또 청소하지 않으며, 벽을 통과할 수 없다.

d가 0인 경우에는 북쪽을, 1인 경우에는 동쪽을, 2인 경우에는 남쪽을, 3인 경우에는 서쪽을 바라보고 있는 것이다.
'''

# 북, 동, 남, 서
# 방향 벡터
dx = [-1, 0, 1, 0]  # 세로축, 행
dy = [0, 1, 0, -1]  # 가로축, 열

ans = 1
arr[x][y] = 2

find = 0
while(True):
    # 왼쪽 방향의 좌표
    d = moveDirLeft(d)
    nx, ny = move(x, y, d)
    # 왼쪽 방향의 좌표가 청소를 안했을 때, 해당 방향의 좌표로 이동
    if (arr[nx][ny] == 0 and find < 4):
        arr[nx][ny] = 2
        ans += 1
        find = 0
        x, y = nx, ny
    # 왼쪽 방향이 청소가 되어 있을 때, 혹은 벽일 때 direction 옮김
    elif(arr[nx][ny] != 0 and find < 4):
        find += 1
        continue
    # 네 방향 모두 벽이거나 청소가 되어있을 때, 그 방향을 바라본 채로 후진
    elif (find == 4):
        tmpd = d
        moveDirLeft(tmpd)
        moveDirLeft(tmpd)
        #후진할 좌표
        nx, ny = move(x,y,tmpd)
        #후진이 가능한 경우
        if(arr[nx][ny] == 2):
            x,y = nx,ny
            find = 0
        else:
            break

print(ans)

for i in range(N):
    print('')
    for j in range(M):
        print(arr[i][j],end='')




