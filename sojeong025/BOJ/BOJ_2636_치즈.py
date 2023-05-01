'''
녹일 수 있는 치즈를 찾기
=> 치즈를 시작으로 하면 찾기 힘들어짐
=> 공기에서 탐색 시작

(0,0) 시작으로 완전 탐색 -> 녹을 치즈는 또 다시 새로운 공기가 됨
-> 또다시 완전 탐색 이런 과정을 반복
'''

from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    q = deque()
    q.append((0,0))
    visited = [[0] * m for _ in range(n)]
    cnt = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0 and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append((nx,ny))
                elif graph[nx][ny] == 1:
                    # queue에 추가해주는게 아니라 0으로 바꿔줘 녹게 만들어줌
                    graph[nx][ny] = 0
                    cnt += 1
                    visited[nx][ny] = 1
    return cnt

result = []
time = 0
while True:
    cnt = bfs()
    result.append(cnt)
    if cnt == 0:
        break
    time += 1

print(time)
print(result[-2])