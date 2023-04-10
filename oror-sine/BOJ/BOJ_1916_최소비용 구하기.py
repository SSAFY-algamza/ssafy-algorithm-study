import sys
from collections import deque

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
infos = [[] for _ in range(N+1)]
for _ in range(M):
    s, e, c = map(int, sys.stdin.readline().split())
    infos[s].append((c, e))
S, E = map(int, sys.stdin.readline().split())
costs = [1e8]*(N+1)
costs[S] = 0
Q = deque()
Q.append(S)

while Q:
    s = Q.popleft()
    for c, e in sorted(infos[s]):
        if costs[e] > costs[s] + c:
            costs[e] = costs[s] + c
            Q.append(e)

print(costs[E])
