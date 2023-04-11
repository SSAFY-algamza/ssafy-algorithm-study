from collections import deque
delta = [(-1,0),(1,0),(0,-1),(0,1)]
def bfs(x,y):
    q = deque([(x, y, 1, 0)])
    while q:
        x, y, cnt, isBreak = q.popleft()
        if (x, y) == (N-1, M-1):
            return cnt
        for i in range(4):
            nx, ny = x+delta[i][0], y+delta[i][1]
            if 0 <= nx < N and 0 <= ny < M:
                if table[nx][ny] == '1' and not isBreak and visited[nx][ny]==[0,0]:
                    visited[nx][ny][1] = 1
                    q.append((nx, ny, cnt+1, 1))
                elif table[nx][ny] == '0' and not visited[nx][ny][isBreak]:
                    visited[nx][ny][isBreak] = 1
                    q.append((nx, ny, cnt+1, isBreak))
    return -1

N, M = map(int, input().split())
table = [list(input()) for _ in range(N)]
# visited => 현재좌표에 벽을 부수고 방문했냐 / 벽을 안부수고 방문했냐
visited = [[[0,0] for _ in range(M)] for _ in range(N)]
visited[0][0][0] = 1
print(bfs(0,0))