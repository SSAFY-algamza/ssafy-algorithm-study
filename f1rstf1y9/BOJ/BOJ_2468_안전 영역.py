dy = [-1,1,0,0]
dx = [0,0,-1,1]

def bfs(y ,x):
    q = [(y ,x)]
    while q:
        y, x = q.pop()
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx]:
                visited[ny][nx] = 1
                if heights[ny][nx] > 0:
                    q.append((ny, nx))

N = int(input())
heights = [list(map(int, input().split())) for _ in range(N)]
survive_cnt = N*N
max_cnt = 1

while survive_cnt:
    for i in range(N):
        for j in range(N):
            if heights[i][j]:
                heights[i][j] -= 1
                if not heights[i][j]:
                    survive_cnt -= 1
    visited = [[0]*N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if heights[i][j] and not visited[i][j]:
                cnt += 1
                visited[i][j] = 1
                bfs(i,j)
    max_cnt = max(max_cnt, cnt)
print(max_cnt)