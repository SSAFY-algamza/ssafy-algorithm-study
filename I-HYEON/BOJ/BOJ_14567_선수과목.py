from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int,input().split())
temp = [0 for _ in range(N+1)]
graph = [[] for _ in range(N+1)]

for _ in range(M):
    A,B = map(int,input().split())
    graph[A].append(B)
    temp[B] += 1

Q = deque([])
result = [0 for _ in range(N+1)]
for i in range(1,N+1):
    if temp[i] ==0:
        Q.append(i)
        result[i] = 1

while Q:
    now = Q.popleft()

    for i in graph[now]:
        temp[i] -= 1
        if temp[i] == 0:
            Q.append(i)
            result[i] = result[now] + 1

ans = result[1:]
print(*ans)
