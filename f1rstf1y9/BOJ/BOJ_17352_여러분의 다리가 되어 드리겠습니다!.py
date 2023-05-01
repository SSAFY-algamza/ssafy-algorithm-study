import sys
input = sys.stdin.readline

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

N = int(input())
parent = [i for i in range(N+1)]
for _ in range(N-2):
    a, b = map(int, input().split())
    union(a, b)

p = parent[1]
for i in range(2, N+1):
    if find_parent(i) != p:
        print(1, i)
        break