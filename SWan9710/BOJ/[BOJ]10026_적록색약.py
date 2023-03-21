dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def DFS(x, y, num, arr, visited):
    stack = [(x, y)]
    visited[x][y] = num

    while stack:
        sx, sy = stack.pop()
        for k in range(4):
            nx, ny = sx + dx[k], sy + dy[k]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                if arr[sx][sy] == arr[nx][ny]:
                    visited[nx][ny] = num
                    stack.append((nx, ny))

    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                DFS(i, j, num+1, arr, visited)

N = int(input())
arr = [list(input()) for _ in range(N)]
arr2 = [[''] * N for _ in range(N)]
visited = [[0] * N for _ in range(N)]
visited2 = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if arr[i][j] == 'R':
            arr2[i][j] = 'G'
        else:
            arr2[i][j] = arr[i][j]

DFS(0,0,1,arr,visited)
DFS(0,0,1,arr2,visited2)

result = 0
result2 = 0

for i in range(N):
    for j in range(N):
        if visited[i][j] > result:
            result = visited[i][j]
        if visited2[i][j] > result2:
            result2 = visited2[i][j]

print(result, result2)