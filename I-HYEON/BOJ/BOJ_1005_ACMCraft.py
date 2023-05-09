import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

for tc in range(1, T + 1):
    n, k = map(int, input().split())
    building_time = [0] + list(map(int, input().split()))
    in_degree = [0 for _ in range(n + 1)]
    graph = [[] for _ in range(n + 1)]
    for _ in range(k):
        x, y = map(int, input().split())
        in_degree[y] += 1
        graph[x].append(y)
    w = int(input())

    Q = deque([])
    ans = [0 for _ in range(n + 1)]
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            Q.append(i)  # 진입차수가 0인 노드들을 담는다
            ans[i] = building_time[i]  # 초기값을 세팅한다

    while Q:
        now = Q.popleft()

        for i in graph[now]:
            in_degree[i] -= 1
            ans[i] = max(ans[i], ans[now] + building_time[i])
            if in_degree[i] == 0:
                Q.append(i)

    print(ans[w])