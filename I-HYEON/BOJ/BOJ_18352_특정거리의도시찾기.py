'''
다익스트라 함수를 수행하고
수행 결과 리스트 v의 원소가 k와 동일한 원소의 인덱스를 출력한다
'''

import sys
import heapq
input = sys.stdin.readline

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))

    while q:
        dist, node = heapq.heappop(q)

        if dist > v[node]:
            continue

        for x in graph[node]:
            cost = x[1] + dist

            if v[x[0]] > cost:
                v[x[0]] = cost
                heapq.heappush(q, (cost, x[0]))
    return

N, M, K, X = map(int,input().split())
graph = [[] for _ in range(N+1)]  # 노드 별로 인접 노드 기록할 리스트
v = [float('inf')]*(N+1)   # 최단 경로 기록 예정. 무한대 로 초기화
v[X] = 0  # 출발 노드 에 기록된 최단 경로는 0 으로 시작

for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append((e, 1))  # 인접 노드와 가중치 어펜드

dijkstra(X)

isNone = 1
for i in range(len(v)):
    if v[i] == K:
        print(i)
        isNone = 0
else:
    if isNone:
        print(-1)

# isNone = 1
# for i in range(1, N+1):
#     if v[i] == K:
#         isNone = 0
#         print(i)
#
# if isNone:
#     print(-1)



'''

        
마지막에 print 방식을 이렇게 하면 시간초과 가 난다. 왜그렇지?
'''