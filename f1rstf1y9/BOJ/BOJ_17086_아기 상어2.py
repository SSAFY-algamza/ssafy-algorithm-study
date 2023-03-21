dy = [-1, 1, 0, 0, 1, 1, -1, -1]
dx = [0, 0, -1, 1, 1, -1, 1, -1]

def bfs(y,x):
    q = [(y,x,0)]
    while q:
        y, x, n = q.pop()
        for i in range(8):
            ny, nx = y+dy[i], x+dx[i]
            if 0 <= ny < N and 0 <= nx < M and visited[ny][nx] > n+1:
                if space[ny][nx]:
                    continue
                visited[ny][nx] = n+1
                q.append((ny,nx,n+1))

N, M = map(int, input().split())
space = [list(map(int, input().split())) for _ in range(N)]
visited = [[M*N] * M for _ in range(N)]
max_safe = 0
for i in range(N):
    for j in range(M):
        if space[i][j] == 1:
            visited[i][j] = 0
            bfs(i,j)
for v in visited:
    max_safe = max(max(v), max_safe)
print(max_safe)
