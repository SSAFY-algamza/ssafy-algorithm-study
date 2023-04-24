import sys, heapq
input = sys.stdin.readline
# sys.stdin = open("input.in", "r")

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    while q:
        cost_now, node_now = heapq.heappop(q)

        if cost_now > feeds[node_now]:
            continue
        for n, w in graph[node_now]:
            cost_next = cost_now + w
            if feeds[n] > cost_next:
                feeds[n] = cost_next
                heapq.heappush(q, (cost_next, n))
    return

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]  # 인접 리스트 생성
for _ in range(M):
    A, B, W = map(int, input().split())
    graph[A].append((B, W))
    graph[B].append((A, W))

feeds = [float('inf')]*(N+1)  # ( 인덱스마다 해당 인덱스까지의 ) 최소 여물을 저장할 리스트. 무한대 초기화.
feeds[1] = 0  # 시작점은 0 으로 초기화

dijkstra(1)  # 시작점을 주고 다익스트라 알고리즘 수행

print(feeds[N])  # 도착점 에 기록된 최소 여물을 프린트