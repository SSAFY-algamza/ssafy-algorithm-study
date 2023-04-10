# def dijkstra(now):
#     # 방문 정보 표기
#     visited = [0] * (V+1)
#     visited[now] = 1
#
#     # 인접 행렬 정보 기반, 첫 시작 지점에서 각 노드별 방문 가능 거리 기록
#     for next in range(V+1):
#         distance[next] = arr[now][next]
#
#     for _ in range(V):
#         w = 0
#         minV = 1e9
#
#         for i in range(V+1):
#             if visited[i] == 0 and minV > distance[i]:
#                 minV = distance[i]
#                 w = i
#         visited[w] = 1
#
#         # 정점 v에 대해
#         for v in range(V+1):
#             # w와 인접 노드이면서,
#             if 0 < arr[w][v] < 1e9:
#                 # 시작점점에서부터 정점 w를 거져 v로 가는 비용과
#                 # 시작지점에서 v로 가는데 걸리는 비용중, 최솟값 갱신
#                 distance[v] = min(distance[v], distance[w] + arr[w][v])
#
# # 노드, 간선, 거리정보, 출발번호
# V, E, K, X =  map(int, input().split())
#
# # 최소 비용을 기록할 것이므로 첫 초기화시에는 최댓값으로 초기화
# arr = [[1e9] * (V+1) for _ in range(V+1)]
#
# # 각 노드에 도착하는 최소 거리 기록
# distance = [0] * (V+1)
#
# for i in range(V+1):
#     # 내 위치 == 이동불가
#     arr[i][i] = 0
#
# # 모든 도로의 거리는 1
# for _ in range(E):
#     # 진출 노드, 진입 노드, 가중치
#     s, e  = map(int, input().split())
#     # 방향이 있는 그래프 이므르 s에서 출발해서 e에 도착
#     arr[s][e] = 1
#
# dijkstra(X)
# count = 0
# for i in distance:
#     if i == K:
#         print(count)
#     count += 1
#
# if K not in distance:
#     print(-1)

# 다익스트라로 했는데 메모리초과 떠서 heapq 써야 겠는데 어찌 써야할지 모르겠다


import sys
from collections import deque

input = sys.stdin.readline

def BFS(start):
    queue = deque([start])

    while queue:
        # 현재위치를 queue의 첫번째 값으로 가져오기
        now = queue.popleft()

        # 다음으로 올 값은 graph리스트의 현재우치
        for next in graph[now]:
            # 방문한 적이 없다면 누적방문 찍어주기
            if visited[next] == -1:
                visited[next] = visited[now] + 1

                # queue에 next값 넣어주기
                queue.append(next)

# 노드, 간선, 거리정보, 출발번호
V, E, K, X = map(int, input().split())
# 2차원 배열로 graph 그려주기
graph = [[] for _ in range(V+1)]

for _ in range(E):
    s, e = map(int,input().split())
    # 방향성이 있는 그래프 이므로 시작넘버 s의 리스트에 e 값 넣어주기
    graph[s].append(e)

# 누적방문 횟수를 찍기위한 visited
visited = [-1] * (V+1)
# 시작부분 0으로 초기화
visited[X] = 0
BFS(X)
# print(visited)
if K in visited:
    for i in range(1, V+1):
        if visited[i] == K:
            print(i)

else:
    print(-1)