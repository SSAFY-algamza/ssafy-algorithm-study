import sys
sys.stdin = open('input.txt')

from collections import deque

row, col = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(col)]
queue = deque([])


for i in range(col):
    for j in range(row):
        if tomato[i][j] == 1:
            queue.append([i, j])

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


def BFS():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < col and 0 <= ny < row and tomato[nx][ny] == 0:
                tomato[nx][ny] = tomato[x][y] + 1
                queue.append([nx, ny])


BFS()
result = 0
for i in range(col):
    for j in range(row):
        if tomato[i][j] == 0:
            print(-1)
            exit()
        else:
            if tomato[i][j] > result:
                result = tomato[i][j]
                result = result - 1
print(result)







