import sys
from collections import deque

ds = ((-1, 0), (1, 0), (0, -1), (0, 1))
p = 1
while True:
    N = int(sys.stdin.readline())
    if N == 0:
        break
    
    costs = [[int(i) for i in sys.stdin.readline().split()] for _ in range(N)]
    totals = [[1e6]*N for _ in range(N)]
    totals[0][0] = costs[0][0]
    Q = deque()
    Q.append((0, 0))
    
    while Q:
        r, c = Q.popleft()
        for dr, dc in ds:
            nr, nc = r+dr, c+dc
            if 0 <= nr < N and 0 <= nc < N:
                if totals[nr][nc] > totals[r][c]+costs[nr][nc]:
                    totals[nr][nc] = totals[r][c]+costs[nr][nc]
                    Q.append((nr, nc))

    print(f'Problem {p}:', totals[-1][-1])
    p += 1