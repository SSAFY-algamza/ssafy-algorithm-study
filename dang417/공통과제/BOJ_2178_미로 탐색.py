import sys
sys.stdin = open('input.txt')

from collections import deque

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def BFS(start):
    global visited
    q = deque()
    q.append(start)
    while q:
        i, j = q.popleft()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < n and 0 <= nj < m:
                if maze[ni][nj] == '1' and not visited[ni][nj]:
                    q.append((ni, nj))
                    visited[ni][nj] = visited[i][j] + 1

n, m = map(int, input().split())

maze = [list(input()) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
start = (0, 0)
visited[0][0] = 1
BFS(start)
print(visited[n-1][m-1])