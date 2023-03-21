'''
인접한 아기상어와의 거리중 가장 큰 값 구하기
조건 1. 빈 칸과 상어의 수가 각각 한 개 이상인 입력만 주어진다.
조건 2. 이동가능한 방향은 인접한 8방향
조건 3. 한 칸에는 아기 상어가 최대 1마리만 존재
'''
import sys
sys.stdin = open('input.txt')

# 8방향 델타탐색
dx = [0,0,1,-1,-1,-1,1,1]
dy = [1,-1,0,0,-1,1,1,-1]

def BFS(x,y):
    queue = [(x,y,0)]

    while queue:
        x, y, num = queue.pop(0)

        for k in range(8):
            nx, ny = x+dx[k], y+dy[k]

            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] > num+1:
                if arr[nx][ny]==1:
                    continue
                visited[nx][ny] = num+1
                queue.append((nx,ny,num+1))


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[N*M] * M for _ in range(N)]
result = 0

for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            visited[i][j] = 0
            BFS(i,j)

for i in visited:
    result = max(max(i), result)
print(result)



