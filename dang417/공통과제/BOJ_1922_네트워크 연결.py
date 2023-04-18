import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

def find_set(x):
    while x != parent[x]:
        x = parent[x]
    return x

def union(x, y):
    parent[find_set(y)] = find_set(x)


N = int(input().rstrip())
M = int(input().rstrip())
rlt = 0

edge = [list(map(int, input().rstrip().split())) for _ in range(M)]
edge.sort(key=lambda x: x[2])

parent = list(range(N+1))

for s, e, w in edge:
    if find_set(s) != find_set(e):
        union(s, e)
        rlt += w

print(rlt)