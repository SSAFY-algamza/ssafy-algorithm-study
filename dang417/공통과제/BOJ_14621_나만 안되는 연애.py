import sys
sys.stdin = open('input.txt')

# MST
# 경로는 gender가 서로 다른곳만 연결된다. 주어지는 것은 모두 주어짐
import sys
input = sys.stdin.readline

def find_set(x):
    while x != parent[x]:
        x = parent[x]
    return x

def union(x, y):
    parent[find_set(y)] = find_set(x)

N, M = map(int, input().rstrip().split())
gender = list(input().rstrip().split())

graph = []
for _ in range(M):
    u, v, d = map(int, input().rstrip().split())
    graph.append((d, u, v))
graph.sort()
parent = list(range(N+1))

rlt = 0
cnt = 0
for w, s, e in graph:
    if find_set(s) != find_set(e) and gender[s-1] != gender[e-1]:
        union(s, e)
        rlt += w
        cnt += 1

if cnt != N-1:
    print(-1)
else:
    print(rlt)