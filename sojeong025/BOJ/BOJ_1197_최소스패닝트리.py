import sys
input = sys.stdin.readline

V, E = map(int, input().split())

parent = [i for i in range(V+1)]

edges = [tuple(map(int, input().split())) for _ in range(E)]
edges.sort(key=lambda x: x[2])


def find_parent(n):
    if parent[n] != n:
        parent[n] = find_parent(parent[n])
    return parent[n]


def union(a, b):
    a, b = find_parent(a), find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


result = 0
for edge in edges:
    a, b, cost = edge
    if find_parent(a) != find_parent(b):
        union(a, b)
        result += cost

print(result)