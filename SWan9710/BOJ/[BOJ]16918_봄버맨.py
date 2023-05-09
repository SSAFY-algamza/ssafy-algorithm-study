import sys
input = sys.stdin.readline
from collections import deque

dx = [1,-1,0,0]
dy = [0,0,1,-1]

# 1단계 폭탄위치 넣어주기
def find_bomb():
    for i in range(R):
        for j in range(C):
            if arr[i][j] == 'O':
                bomb.append((i, j))

# 4단계 폭탄 터트리기
def boom():
    while bomb:
        sx, sy = bomb.popleft()
        arr[sx][sy] = '.'
        for k in range(4):
            nx, ny = sx + dx[k], sy + dy[k]
            if 0 <= nx < R and 0 <= ny < C:
                arr[nx][ny] = '.'

# 3단계 빈칸에 폭탄 채우기
def set_bomb():
    for i in range(R):
        for j in range(C):
            if arr[i][j] == '.':
                arr[i][j] = 'O'
            
R, C, N = map(int,input().split())
arr = [list(map(str, input().strip())) for _ in range(R)]
bomb = deque()

# 2단계 봄버맨 활동 X
N -= 1

while N:
    # 기존폭탄 위치찾기
    find_bomb()
    
    # 3단계 실행
    set_bomb()
    N -= 1

    # 종료조건 --> 시간이 최초로 감소하는 지점
    if N == 0:
        break

    # 4단계 실행
    boom()
    N -= 1

for i in arr:
    print("".join(i))