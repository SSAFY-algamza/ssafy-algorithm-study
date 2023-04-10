import sys
input = sys.stdin.readline

from collections import deque

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

max_res = 0
res = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            res += 1

def count_wall(cnt):
    if cnt == 3:
        bfs()
        return
    
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                arr[i][j] = 1
                count_wall(cnt + 1)
                arr[i][j] = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    global max_res
    visited = [[0] * M for _ in range(N)]
    count = 0
    queue = deque()

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 2:
                visited[i][j] = 1
                queue.append((i, j))

    while queue:
        x, y = queue.popleft()
            
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 > nx or N <= nx or 0 > ny or M <= ny:
                continue
            else:
                if visited[nx][ny] ==0:
                    if arr[nx][ny] == 0:
                        visited[nx][ny] = 1
                        count += 1
                        queue.append((nx, ny))
    max_res = max(max_res,  res - count)

count_wall(0)
print(max_res - 3)