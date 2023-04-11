import sys
sys.stdin = open('input.txt')

import heapq

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    total[start] = 0
    while q:
        to, now = heapq.heappop(q)

        if total[now] < to:
            continue

        for i in graph[now]:
            ans = to + i[1]
            if ans < total[i[0]]:
                total[i[0]] = ans
                heapq.heappush(q, (ans, i[0]))


INF = int(1e9)
# N : 헛간 갯수 M : 소들의 길 갯수
N, M = map(int, input().split())

graph = [[] for i in range(N+1)]
total = [INF] * (N+1)

for _ in range(M):
    s, e, w = map(int, input().split())

    graph[s].append((e,w))
    graph[e].append((s,w))

dijkstra(1)
print(total[N])
