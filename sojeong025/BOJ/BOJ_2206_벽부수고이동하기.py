# import sys
# sys.stdin = open('input.txt')
# input = sys.stdin.readline

from collections import deque

n,m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    q = deque()
    q.append([0, 0, 1])
    # 3차원 리스트 (행, 열, 벽을 깬 여부) 생성
    visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
    visited[0][0][1] = 1

    while q:
        x, y, wall = q.popleft()
        if x == n-1 and y == m-1:
            return visited[x][y][wall]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if graph[nx][ny] == 0 and visited[nx][ny][wall] == 0:
                visited[nx][ny][wall] = visited[x][y][wall] +1
                q.append((nx, ny, wall))
            elif graph[nx][ny] == 1 and wall ==1:
                visited[nx][ny][0] = visited[x][y][wall] + 1
                q.append((nx, ny, 0))
    return -1
print(bfs())
