from collections import deque
import sys
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def BFS(i ,j):
    # 빙산 덩어리 세주기
    global count

    queue = deque([(i, j)])
    visited[i][j] = 1

    while queue:
        sx, sy = queue.popleft()
        for k in range(4):
            nx, ny = sx + dx[k], sy + dy[k]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                if arr[nx][ny] != 0:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))

                # 빙산이 아닌경우 주변이 바닷물 이므로 4면중 1명이 바닷물에 닿았다는 뜻
                # 전체 BFS를 돌고나서 한번에 빙산을 녹여줄 거니까 배열에 값 더해주기
                else:
                    minus[sx][sy] += 1

    # BFS를 다 돌았다면 그건 빙산이라는 뜻
    # 빙산갯수 + 1
    count += 1

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
year = 0

# 모든 빙산이 녹을때까지 반복
while True:
    # 최초 빙산의 갯수
    count = 0
    # 전체 배열에서 - 해줄 배열값을 저장할거
    minus = [[0] * M for _ in range(N)]
    visited = [[0] * M for _ in range(N)]

    # 빙산일때 BFS 실시하며 minus 배열 채워주기
    for i in range(N):
        for j in range(M):
            if arr[i][j] != 0 and not visited[i][j]:
                BFS(i, j)

    # 빙산 깍기
    for i in range(N):
        for j in range(M):
            arr[i][j] -= minus[i][j]
            if arr[i][j] < 0:
                arr[i][j] = 0

    # 종료조건
    if count == 0 or count >= 2:
        break

    # 끝까지 다 돌았으면 년수 + 1
    year += 1

# 빙산 갯수가 2개 이상인 경우
if count >= 2:
    print(year)
else:
    print(0)