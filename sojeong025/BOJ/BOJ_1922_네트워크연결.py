import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

parent = [i for i in range(n+1)]
edges = [tuple(map(int, input().split())) for _ in range(m)]
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