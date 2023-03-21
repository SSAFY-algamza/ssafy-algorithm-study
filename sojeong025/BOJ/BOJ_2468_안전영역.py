from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def DFS(x, y, h):
    cnt = 1
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        visited[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 > nx or nx >= N or 0 > ny or ny >= N:
                continue
            if visited[nx][ny] == 0 and height[nx][ny] > h:
                q.append((nx, ny))
                cnt += 1
                visited[nx][ny] = 1
    return cnt

N = int(input())
cnt = 0
res = 0
height = [list(map(int, input().split())) for _ in range(N)]
water_max = 0
for i in range(N):
    for j in range(N):
        water_max = max(water_max, height[i][j])

for h in range(water_max+1):
    visited = [[0]*N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0 and height[i][j] > h:
                cnt += 1
                DFS(i, j, h)
    res = max(res, cnt)
    if cnt == 0:
        break
print(res)
