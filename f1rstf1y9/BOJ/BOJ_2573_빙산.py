from collections import deque

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

delta = [(-1,0),(1,0),(0,-1),(0,1)]
def melt(x,y):
    cnt = 0
    for dx, dy in delta:
        nx, ny = x+dx, y+dy
        if 0 <= nx < N and 0 <= ny < M and not grid[nx][ny]:
            cnt += 1
    temp = grid[x][y]-cnt
    melted.append((x,y,temp if temp > 0 else 0))
    return melted[-1][2]

def isDivided(ice, x, y):
    q = deque([(x, y)])
    cnt = 1
    while q:
        x, y = q.popleft()
        visited[x][y] = True
        for dx, dy in delta:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                if grid[nx][ny]:
                    visited[nx][ny] = True
                    cnt += 1
                    q.append((nx, ny))
    return cnt != ice

year = 0
while True:
    year += 1
    ice = 0
    ix, iy = 0, 0
    melted = []
    for i in range(N):
        for j in range(M):
            if grid[i][j]:
                if melt(i,j):
                    ice += 1
                    ix, iy = i, j

    for x, y, i in melted:
        grid[x][y] = i

    visited = [[False] * M for _ in range(N)]
    visited[ix][iy] = True

    if ice == 0:
        print(0)
        break

    if isDivided(ice, ix, iy):
        print(year)
        break
