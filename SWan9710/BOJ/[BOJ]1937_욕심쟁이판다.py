import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def DFS(x, y):
    # 종료조건
    # 방문기록이 있다면 종료
    if visited[x][y] != 0:
        return visited[x][y]
    
    # 방문기록이 없을경우 아래 코드 실행
    visited[x][y] = 1   # 방문표시
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < N and 0 <= ny < N:
            if arr[nx][ny] > arr[x][y]:
                # 조건에 맞다면 방문기록 남기는데 제일 긴 거리 방문기록으로 남기기
                # 시작지점값도 더해줘야 해서 DFS + 1 해주기
                visited[x][y] = max(visited[x][y], DFS(nx, ny)+1)
    
    # 방문기록 없는데 if 조건 안맞아서 종료되는 경우
    return visited[x][y]

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
result = []
for i in range(N):
    for j in range(N):
        result.append(DFS(i, j))
print(max(result))
