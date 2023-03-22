import sys
from collections import deque
ds = ((-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1))
N, M = map(int, sys.stdin.readline().split())
grid = [[True if i == "0" else False for i in sys.stdin.readline().split()] for _ in range(N)]


def bfs(coord):
    Q = deque([coord])
    visited = [[False]*M for _ in range(N)]
    visited[coord[0]][coord[1]] = True
    cnt = 0
    while Q:
        cnt += 1
        for _ in range(len(Q)):
            r, c = Q.popleft()
            for dr, dc in ds:
                if 0 <= (nr:= r+dr) < N and 0 <= (nc:= c+dc) < M and not visited[nr][nc]:
                    if not grid[nr][nc]:
                        return cnt
                    visited[nr][nc] = True
                    Q.append((nr, nc))


maxi = 0
for r in range(N):
    for c in range(M):
        if grid[r][c]:
            if maxi < (safe_distance := bfs((r, c))):
                maxi = safe_distance

print(maxi)