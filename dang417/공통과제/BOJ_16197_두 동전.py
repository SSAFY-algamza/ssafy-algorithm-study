import sys
sys.stdin = open('input.txt')

from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def BFS():
    while q:
        x1, y1, x2, y2, cnt = q.popleft()

        if cnt >= 10:
            return -1

        for k in range(4):
            nx1 = x1 + dx[k]
            ny1 = y1 + dy[k]
            nx2 = x2 + dx[k]
            ny2 = y2 + dy[k]

            if 0 <= nx1 < N and 0 <= ny1 < M and 0 <= nx2 < N and 0 <= ny2 < M:
                if board[nx1][ny1] == '#':
                    nx1, ny1 = x1, y1
                if board[nx2][ny2] == '#':
                    nx2, ny2 = x2, y2
                q.append((nx1, ny1, nx2, ny2, cnt+1))

            elif 0 <= nx1 < N and 0 <= ny1 < M:
                return cnt + 1

            elif 0 <= nx2 < N and 0 <= ny2 < M:
                return cnt + 1

            else:
                continue

N, M = map(int, input().split())
board = [[0] * M for _ in range(N)]
coins = []

for i in range(N):
    board[i] = list(input().strip())
    for j in range(M):
        if board[i][j] == 'o':
            coins.append((i, j))

q = deque()
q.append((coins[0][0], coins[0][1], coins[1][0], coins[1][1], 0))

print(BFS())

