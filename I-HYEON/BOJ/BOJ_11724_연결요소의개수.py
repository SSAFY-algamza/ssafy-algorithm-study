from collections import deque
import sys

input = sys.stdin.readline

V, E = map(int, input().split())
visited = [0 for _ in range(V+1)]
graph = [[] for _ in range(V+1)]
for _ in range(E):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

def BFS(start):
    Q = deque([])
    Q.append(start)
    visited[start] = 1  # 방문표시하고 출발

    while Q:
        now = Q.popleft()

        for i in graph[now]:
            if not visited[i]:
                Q.append(i)
                visited[i] = 1
    return

cnt = 0
for i in range(1, V+1):
    if not visited[i]:
        BFS(i)
        cnt += 1

print(cnt)