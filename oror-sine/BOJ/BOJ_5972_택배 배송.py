import sys, heapq

N, M = map(int, sys.stdin.readline().split())
costs = [50_000_000]*(N+1)
costs[1] = 0
roads = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    heapq.heappush(roads[a], (c, b))
    heapq.heappush(roads[b], (c, a))

heap = [(0, 1)]

while heap:
    _, s = heapq.heappop(heap)
    for _ in range(len(roads[s])):
        c, e = heapq.heappop(roads[s])
        ncost = costs[s] + c
        if costs[e] > ncost:
            costs[e] = ncost
            heapq.heappush(heap, (costs[e], e))

print(costs[N])
