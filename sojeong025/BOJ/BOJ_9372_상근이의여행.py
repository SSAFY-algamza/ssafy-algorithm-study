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


T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    parent = [i for i in range(N+1)]

    result = 0
    for edge in range(M):
        a, b = map(int, input().split())
        if find_parent(a) != find_parent(b):
            union(a, b)
            result += 1
    print(result)
