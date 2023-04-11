import sys
input = sys.stdin.readline
# sys.stdin = open('input.txt')
from collections import deque

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque()
def bfs(x, y):
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()
        visited[x][y] = 1
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 > nx or N <= nx or 0 > ny or M <= ny:
                continue
            else:
                if visited[nx][ny] == 0 and arr[nx][ny] != 0:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))
                elif arr[nx][ny] == 0:
                    melt[x][y] += 1
    return 1


day = 0
flag = 0

while True:
    visited = [[0] * M for _ in range(N)]
    melt = [[0] * M for _ in range(N)]
    ice = []

    for i in range(N):
        for j in range(M):
            if arr[i][j] != 0 and visited[i][j] == 0:
                ice.append(bfs(i, j))
    
    for i in range(N):
        for j in range(M):
            arr[i][j] -= melt[i][j]
            if arr[i][j] < 0:
                arr[i][j] = 0
    # print(ice)
    if len(ice) == 0:
        break
    elif len(ice) >= 2:
        flag = 1
        break
    day += 1

if flag == 1:
    print(day)
elif flag == 0:
    print(0)

                





    