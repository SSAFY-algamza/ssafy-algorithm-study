import sys


def solution():
    N, M = map(int, sys.stdin.readline().split())
    maze = [[1-int(i) for i in sys.stdin.readline().rstrip()]
            for _ in range(N)]
    Q = [(0, 0)]
    maze[0][0] = 1
    while Q:
        r, c = Q.pop(0)
        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            if 0 <= (nr := r+dr) < N and 0 <= (nc := c+dc) < M and maze[nr][nc] == 0:
                maze[nr][nc] = maze[r][c]+1
                Q.append((nr, nc))
    return maze[N-1][M-1]


print(solution())
