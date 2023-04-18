import sys
from heapq import heappush, heappop
input = sys.stdin.readline
INF = int(1e9)

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]
for i in range(M):
    s, e, c = map(int, input().split())
    graph[s].append((e, c))

start, end = map(int, input().split())

dist = [INF]*(N+1)
def dijkstra(start):
    dist[start] = 0
    heapq = [(0, start)]

    while heapq:
        w, cur = heappop(heapq)
        if dist[cur] < w: #이미 처리되었다면 무시
            continue

        for dest, wei in graph[cur]:
            cost = dist[cur] + wei
            if dist[dest] > cost:
                dist[dest] = cost
                heappush(heapq, (cost, dest))

dijkstra(start)
print(dist[end])