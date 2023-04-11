delta = [(-1,0),(1,0),(0,-1),(0,1)]

def bt(x, y, n, total):
    global ans
    if n == 4:
        ans = max(total, ans)
        return
    for dx, dy in delta:
        nx, ny = x+dx, y+dy
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
            if n == 2:
                visited[nx][ny] = 1
                bt(x, y, n+1, total+grid[nx][ny])
                visited[nx][ny]
            visited[nx][ny] = 1
            bt(nx, ny, n+1, total+grid[nx][ny])
            visited[nx][ny] = 0

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
ans = 0

for i in range(N):
    for j in range(M):
        visited[i][j] = 1
        bt(i, j, 1, grid[i][j])
        visited[i][j] = 0
print(ans)
