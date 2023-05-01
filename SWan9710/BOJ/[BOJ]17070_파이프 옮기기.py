'''
파이프가 직각으로 꺾이는 경우 X
가로이동일 경우 가능한 방향 가로와 대각선아래
세로이동일 경우 가능한 방향 세로와 대각선아래
대각선이동일 경우 가능한 방향 가로 세로 대각선 아래
'''
import sys
input = sys.stdin.readline
count = 0
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# move 0: 가로, 1: 세로 , 2: 대각선
def DFS(x,y,move):
    global count
    # 종료조건
    if x == N - 1 and y == N - 1:
        count += 1
        return

    # 가로이동
    if move == 0:
        # 가로로 끝까지 이동해서 벽에 닿은경우
        if y == N - 1:
            return

        # 가로 이동
        if 0 <= x < N and 0 <= y + 1 < N and arr[x][y + 1] == 0:
            DFS(x, y + 1, 0)

        # 대각선 이동
        if 0 <= x + 1 < N and 0 <= y + 1 < N:
            if arr[x][y + 1] == 0 and arr[x + 1][y] == 0 and arr[x + 1][y + 1] == 0:
                DFS(x + 1, y + 1, 2)

    # 세로이동
    elif move == 1:
        # 아래로 끝까지 내려간경우
        if x == N - 1:
            return

        # 세로이동
        if 0 <= x + 1 < N and 0 <= y < N and arr[x + 1][y] == 0:
            DFS(x + 1, y, 1)

        # 대각선 이동
        if 0 <= x + 1 < N and 0 <= y + 1 < N:
            if arr[x][y + 1] == 0 and arr[x + 1][y] == 0 and arr[x + 1][y + 1] == 0:
                DFS(x + 1, y + 1, 2)

    # 대각선 이동
    elif move == 2:

        # 가로이동
        if 0 <= x < N and 0 <= y + 1 < N and arr[x][y + 1] == 0:
            DFS(x, y + 1, 0)

        # 세로이동
        if 0 <= x + 1 < N and 0 <= y < N and arr[x + 1][y] == 0:
            DFS(x + 1, y, 1)

        # 대각선 이동
        if 0 <= x + 1 < N and 0 <= y + 1 < N:
            if arr[x][y + 1] == 0 and arr[x + 1][y] == 0 and arr[x + 1][y + 1] == 0:
                DFS(x + 1, y + 1, 2)

# 기본은 가로이동부터
DFS(0,1,0)
print(count)