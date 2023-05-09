import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline
from collections import deque, defaultdict

def light_on(x, y):
    global rlt
    for d in dic[(x, y)]:
        if not light[d[0]][d[1]]:
            light[d[0]][d[1]] = 1
            rlt += 1

def BFS():
    while q:
        x, y = q.popleft()
        light_on(x, y)

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 1 <= nx <= N and 1 <= ny <= N:
                candidate[nx][ny] = 1

        for i in range(1, N + 1):
            for j in range(1, N + 1):
                if not visited[i][j] and light[i][j] and candidate[i][j]:
                    visited[i][j] = 1
                    q.append((i, j))


N, M = map(int, input().split())
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

dic = defaultdict(list)

for _ in range(M):
    x, y, a, b = map(int, input().split())
    dic[(x, y)].append((a, b))

q = deque()
q.append((1, 1))

visited = [[0] * (N + 1) for _ in range(N + 1)]
visited[1][1] = 1

light = [[0] * (N + 1) for _ in range(N + 1)]
light[1][1] = 1

candidate = [[0] * (N + 1) for _ in range(N + 1)]

rlt = 1
BFS()
print(rlt)