import sys
sys.stdin = open('input.txt')

from collections import deque

N, M, V = map(int, input().split())
graph = [[0] * (N+1) for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    # 간선이 양방향이므로 양쪽 설정해두기
    graph[a][b] = 1
    graph[b][a] = 1

# dfs, bfs 각자 방문 기록 체크해야함
dvisited = [0] * (N+1)
bvisited = [0] * (N+1)


def dfs(v):
    dvisited[v] = 1
    d.append(v)
    for i in range(1, N+1):
        if not dvisited[i] and graph[v][i]:
            dfs(i)


def bfs(v):
    q = deque([v])
    while q:
        v = q.popleft()
        if v not in b:
            b.append(v)
        if bvisited[v] == 0:
            bvisited[v] = 1
        for i in range(1, N+1):
            if not bvisited[i] and graph[v][i]:
                bvisited[v] = 1
                q.append(i)

d = []
b = []
dfs(V)
bfs(V)
print(*d)
print(*b)
