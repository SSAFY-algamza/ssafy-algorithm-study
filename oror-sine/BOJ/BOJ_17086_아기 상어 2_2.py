import sys
from collections import deque
ds = ((-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1))
N, M = map(int, sys.stdin.readline().split())
sharks = []
visited = [[False]*M for _ in range(N)]
for r in range(N):
    for c, cell in enumerate(sys.stdin.readline().split()):
        if cell == "1":
            sharks.append((r, c))
            visited[r][c] = True

Q = deque(sharks)
cnt = -1
while Q:
    cnt += 1
    for _ in range(len(Q)):
        r, c = Q.popleft()
        for dr, dc in ds:
            if 0 <= (nr:= r+dr) < N and 0 <= (nc:= c+dc) < M and not visited[nr][nc]:
                visited[nr][nc] = True
                Q.append((nr, nc))
print(cnt)