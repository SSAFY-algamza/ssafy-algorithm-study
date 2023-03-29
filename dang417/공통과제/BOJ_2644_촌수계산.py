import sys
sys.stdin = open('input.txt')

def DFS(now, num):
    num += 1
    visited[now] = 1
    if now == end:
        result.append(num)
        return

    for i in graph[now]:
        if not visited[i]:
            DFS(i, num)
    return

N = int(input())
start, end = map(int, input().split())

M = int(input())
graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)
result = []

for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

DFS(start, 0)

if len(result) == 0:
    print(-1)
else:
    print(result[0] - 1)