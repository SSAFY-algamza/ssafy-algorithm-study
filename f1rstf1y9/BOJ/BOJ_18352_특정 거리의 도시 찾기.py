from heapq import heappush, heappop
import sys
input = sys.stdin.readline

def dijkstra(n):
    q = []
    heappush(q, (0, n))
    dist[n] = 0
    while q:
        d, n = heappop(q)
        if dist[n] < d:
            continue
        for city in graph[n]:
            cost = d + city[1]
            if cost < dist[city[0]]:
                dist[city[0]] = cost
                heappush(q, (cost, city[0]))

N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
dist = [1e9] * (N+1)

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append((B, 1))

dijkstra(X)
isExist = False
for i in range(1, N+1):
    if dist[i] == K:
       print(i)
       isExist = True
if not isExist:
    print(-1)
