import sys, heapq
readline = sys.stdin.readline

def find(rep, x):
    while x != rep[x]:
        x = rep[x]
    return x

def union(rep, a, b):
    A, B = find(rep, a), find(rep, b)
    if A == B: return False
    if A < B: rep[A] = B
    else: rep[B] = A
    return True

V, E = map(int, readline().split())
rep = list(range(V+1))
edges = []
for _ in range(E):
    a, b, c = map(int, readline().split())
    heapq.heappush(edges, (c, a, b))

cnt = cost = 0
for _ in range(E):
    c, a, b = heapq.heappop(edges)
    if union(rep, a, b): 
        cnt += 1
        cost += c
        if cnt == V-1: break
print(cost)
