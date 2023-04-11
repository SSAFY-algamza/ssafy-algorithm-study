import sys
sys.stdin = open('input.txt')

# 힙으로 구현한 다익스트라를 공부해서 다시 풀어보기
# 왜 최댓값을 100000으로 잡으면 틀리는지..?

import sys
import heapq
input = sys.stdin.readline

def dijkstra(start):
    pq = []
    heapq.heappush(pq, (0, start))
    visited[start] = 0

    while pq:
        d, start = heapq.heappop(pq)

        if visited[start] < d:
            continue

        for nw, nx in graph[start]:
            nd = d + nw
            if visited[nx] > nd:
                heapq.heappush(pq, (nd, nx))
                visited[nx] = nd

N = int(input().rstrip())
M = int(input().rstrip())

graph = [[] for _ in range(N+1)]
visited = [1e9] * (N+1)

for _ in range(M):
    s, e, w = map(int, input().rstrip().split())
    graph[s].append((w, e))

A, B = map(int, input().rstrip().split())

dijkstra(A)

print(visited[B])