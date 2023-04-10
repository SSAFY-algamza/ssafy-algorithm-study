import sys
input = sys.stdin.readline
from collections import deque

M, N, H = map(int, input().split())
arr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]


queue = deque()
for i in range(H):
    for j in range(N):
        for k in range(M):
            if arr[i][j][k] == 1:
                queue.append((i, j, k))

while queue:
    z, x, y = queue.popleft()

    for l in range(6):
        nz = z + dz[l]
        nx = x + dx[l]
        ny = y + dy[l]

        if 0 > nz or H <= nz or 0 > nx or N <= nx or 0 > ny or M <= ny :
            continue
        else:
            if arr[nz][nx][ny] == 0:
                arr[nz][nx][ny] = arr[z][x][y] + 1
                queue.append((nz, nx, ny))

day = 1
not_tomato = 0

for a in arr:
    for b in a:
        not_tomato += b.count(0)
        day = max(day, max(b))
        
if not_tomato:
    print(-1)

else:
    if day == 1:
        print(0)
    else:
        print(day-1)