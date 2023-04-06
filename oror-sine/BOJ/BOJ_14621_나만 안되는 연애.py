import sys

N, M = map(int, sys.stdin.readline().split())
univs = [0] + sys.stdin.readline().split()
roads = []
for _ in range(M):
    u, v, d = map(int, sys.stdin.readline().split())
    if univs[u] != univs[v]:
        roads.append((d, u, v))
roads.sort()
rep = [i for i in range(N+1)]


def find_set(x):
    while x != rep[x]:
        x = rep[x]
    return x

ans = 0
cnt = 1
for d, u, v in roads:
    if (a := find_set(u)) != (b := find_set(v)):
        if a > b:
            rep[b] = a
        else:
            rep[a] = b
        ans += d
        cnt += 1
        if cnt == N:
            break

if cnt == N:
    print(ans)
else:
    print(-1)
