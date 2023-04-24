import sys
import heapq
sys.stdin = open("input.in", "r")

N, D = map(int, input().split())
graph = [[] for _ in range(D+1)]

for i in range(D):
    graph[i].append((i+1, 1))  # 크기 D+1인 그래프 생성

for _ in range(N):  # input에 주어진 정보도 그래프에 반영한다
    s, e, w = map(int, input().split())
    if e <= D:
        graph[s].append((e, w))

v = [float('inf')]*(D+1)  # 각 노드마다 최단경로를 기록할 배열, 모두 무한대로 초기화
v[0] = 0
def dijkstra(start):
    q = []
    heapq.heappush(q, start)

    while q:
        now, dist = heapq.heappop(q)
        if v[now] < dist:
            continue

        for node, shortcut in graph[now]:
            if node <= D:
                if v[node] > dist + shortcut:
                    v[node] = dist + shortcut
                    heapq.heappush(q, (node, dist + shortcut))

    return v[D]

print(dijkstra((0, 0)))