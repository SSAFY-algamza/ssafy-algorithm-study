import sys
sys.stdin = open('input.txt')

from collections import deque

n, m = map(int, input().split())
shark = [list(map(int, input().split())) for _ in range(n)]

# 8가지 이동방향
dx = [-1, -1, -1, 0, 1, 0, 1, 1]
dy = [-1, 0, 1, 1, 1, -1, 0, -1]

queue = deque()


def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if not shark[nx][ny]:
                shark[nx][ny] = shark[x][y] + 1
                queue.append((nx, ny))


for i in range(n):
    for j in range(m):
        if shark[i][j] == 1:
            queue.append((i, j))

bfs()
print(max(map(max, shark))-1)
