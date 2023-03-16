import sys
sys.stdin = open('input.txt')
from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def BFS(arr):
    global rlt
    visited = [[0] * n for _ in range(n)]
    q = deque()
    tmp = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] and not visited[i][j]:
                visited[i][j] = 1
                q.append((i, j))
                while q:
                    r, c = q.popleft()
                    for k in range(4):
                        nr = r + dr[k]
                        nc = c + dc[k]
                        if 0 <= nr < n and 0 <= nc < n:
                            if arr[nr][nc] and not visited[nr][nc]:
                                visited[nr][nc] = 1
                                q.append((nr, nc))
                tmp += 1
    if rlt <= tmp:
        rlt = tmp


n = int(input())
area = [list(map(int, input().split())) for _ in range(n)]


rlt = 1
max_v = max(max(area))

for _ in range(max_v):
    BFS(area)
    for i in range(n):
        for j in range(n):
            if area[i][j]:
                area[i][j] -= 1

print(rlt)