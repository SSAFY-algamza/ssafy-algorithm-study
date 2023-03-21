import sys
sys.stdin = open('input.txt')

# 우, 상, 좌, 하 순의로 델타탐색
dx = [0,-1,0,1]
dy = [1,0,-1,0]

def BFS(x, y):
    queue = [(x, y)]
    visited[x][y] = 1

    while queue:
        sx, sy = queue.pop(0)
        for k in range(4):
            nx, ny = sx + dx[k], sy + dy[k]

            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0:
                if arr[nx][ny] == 1:
                    queue.append((nx, ny))
                    # 너비우선 탐색실시 하며 visited에 이전 visited +1 값을 넣어줌
                    visited[nx][ny] = visited[sx][sy] + 1
  
# 배열의 크기 및 종점에 해당
N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

# 너비우선 탐색의 시작지점
BFS(0, 0)
# 출력해야 할 도착지점의 값
print(visited[N-1][M-1])