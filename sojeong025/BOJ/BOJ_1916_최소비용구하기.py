import sys
sys.stdin = open('input.txt')
# input = sys.stdin.readline()
import heapq

def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start))
    cost[start] = 0
    while q:    # 큐가 비어있지 않다면
        # 가장 최소 비용인 노드에 대한 정보 꺼내기
        co, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if cost[now] < co:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            ans = co + i[1]
            # 현재 노드를 거쳐, 다른 노드로 이동하는 거리가 더 짧은 경우
            if ans < cost[i[0]]:
                cost[i[0]] = ans
                heapq.heappush(q, (ans, i[0]))


INF = int(1e9)
N = int(input())    # N : 도시의 개수
M = int(input())    # M : 버스의 개수


# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 생성
graph = [[] for i in range(N+1)]
# 최소 비용 테이블을 모두 무한으로 초기화
cost = [INF] * (N+1)

# 모든 간선 정보 입력받기
for _ in range(M):
    s, e, w = map(int, input().split())
    # s번 노드에서 e번 노드로 가는 비용이 w라는 의미
    graph[s].append((e,w))

start, end = map(int, input().split())

dijkstra(start)
print(cost[end])
