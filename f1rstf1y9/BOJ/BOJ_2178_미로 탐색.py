from collections import deque

dy = [-1,1,0,0]
dx = [0,0,-1,1]

def bfs(y,x):
    q = deque([(y,x,1)])
    while q:
        y, x, n = q.popleft()
        if (y,x) == (N-1,M-1):
            return n
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx]:
                visited[ny][nx] = 1
                if maze[ny][nx]:
                    q.append((ny, nx, n+1))

N, M = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]

ans = bfs(0,0)
print(ans)