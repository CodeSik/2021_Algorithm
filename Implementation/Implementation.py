'''
1. 일반적으로 알고리즘 문제에서의 2차원 공간은 행렬의 의미로 사용된다.
2. 시물레이션 및 완전 탐색 문제에서는 2차원 공간에서의 방향 벡터가 자주 활용된다.
'''

def directionVector():
    for i in range(5):
        print("")
        for j in range(5):
            print(f"({i},{j})", end = ' ')

    #동, 북, 서, 남
    #방향 벡터
    dx = [0, -1, 0, 1] # 세로축, 행
    dy = [1, 0, -1, 0] # 가로축, 열

    x,y = 2,2 # 현재 위치
    print("")
    #2,2 에서 동, 북, 서, 남 순서대로 이동함.
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        print(nx,ny)

def main():
    directionVector()

if __name__ == "__main__":
    main()
