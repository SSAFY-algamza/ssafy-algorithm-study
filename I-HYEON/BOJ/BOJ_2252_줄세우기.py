import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int,input().split())  # 학생 수와 키를 비교한 횟수
lst = [0 for _ in range(n+1)]  # 진입차수 즉, 자신보다 더 키가 작은 학생이 몇명 존재하는지 기록하는 배열
graph = [[] for _ in range(n+1)]  # 단방향 탐색가능한 그래프

for _ in range(m):
    a, b = map(int, input().split())
    lst[b] += 1
    graph[a].append(b)

Q = deque([])  # 큐생성
result = []  # 정답 담을 배열
for i in range(1,n+1):
    if lst[i]==0:  # 진입차수가 0이라면
        Q.append(i)

while Q:
    now = Q.popleft()
    result.append(now)

    for i in graph[now]:
        lst[i] -= 1
        if lst[i] == 0:
            Q.append(i)

print(*result)