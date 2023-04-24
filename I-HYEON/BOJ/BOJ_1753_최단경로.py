import sys
import heapq
input = sys.stdin.readline

def dijkstra(s):
    Q =[]
    heapq.heappush(Q, (0, s))

    while Q:
        dist, node = heapq.heappop(Q)

        if v[node] < dist:  # 지금까지 더해온 거리보다 노드에 적힌 최단경로가 더 작다면
            continue

        for next_node, weight in adj[node]:
            next_dist = dist + weight
            if v[next_node] > next_dist:
                v[next_node] = next_dist
                heapq.heappush(Q, (next_dist, next_node))
    return

V, E = map(int, input().split())
K = int(input())
adj = [[] for _ in range(V+1)]

for _ in range(E):
    s, e, w = map(int, input().split())
    adj[s].append((e, w))

v = [float('inf') for _ in range(V+1)]
v[K] = 0

dijkstra(K)

for i in v[1:]:
    if i == float('inf'):
        print('INF')
    else:
        print(i)
