import heapq
import sys

input = sys.stdin.readline

def dijkstra(s):
    q = []
    heapq.heappush(q,(0,s))

    while q:
        now_cost, now_node = heapq.heappop(q)

        if costs[now_node] < now_cost:
            continue
        for next_node, weight in adj[now_node]:
            next_cost = now_cost + weight

            if costs[next_node] > next_cost:
                costs[next_node] = next_cost
                heapq.heappush(q, (next_cost, next_node))
    return

N = int(input())
M = int(input())
adj = [[] for _ in range(N+1)]
for _ in range(M):
    s, e, w = map(int, input().split())
    adj[s].append((e, w))

S, E = map(int, input().split())
costs = [float('inf')]*(N+1)

dijkstra(S)
print(costs[E])