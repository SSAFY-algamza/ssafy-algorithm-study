import sys
sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n = int(input())
parent = [ i for i in range(n+1)]

for _ in range(n-2):
    a, b = map(int, input().split())
    union(parent, a, b)

ans = []
for i in range(1, n+1):
    if i == parent[i]:
        ans.append(i)

print(*ans)