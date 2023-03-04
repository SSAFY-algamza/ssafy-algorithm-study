import sys
sys.stdin = open('input.txt')

from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def BFS(x, y):
    queue.append((x, y))
    visited[x][y] = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 > nx or N <= nx or 0 > ny or N <= ny:
                continue
            if color[nx][ny] == color[x][y] and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                queue.append((nx, ny))


N = int(input())
color = [list(input()) for _ in range(N)]
queue = deque()

visited = [[0] * N for _ in range(N)]
cnt1 = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            BFS(i, j)
            cnt1 += 1

for i in range(N):
    for j in range(N):
        if color[i][j] == 'R':
            color[i][j] = 'G'
visited = [[0] * N for _ in range(N)]
cnt2 = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            BFS(i, j)
            cnt2 += 1
print(cnt1, cnt2)

