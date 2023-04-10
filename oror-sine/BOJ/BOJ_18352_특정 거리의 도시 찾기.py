import sys
from collections import deque

N, M, K, X = map(int, sys.stdin.readline().split())
adjacency = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    adjacency[A].append(B)

distances = [300_000]*(N+1)
distances[X] = 0
Q = deque()
Q.append(X)
d = 0
ans = []

while Q and d < K:
    d += 1
    for _ in range(len(Q)):
        A = Q.popleft()
        for B in adjacency[A]:
            if distances[B] > d:
                distances[B] = d
                if d == K:
                    ans.append(B)
                    continue
                Q.append(B)

if ans:
    for i in sorted(ans):
        print(i)
else:
    print(-1)
