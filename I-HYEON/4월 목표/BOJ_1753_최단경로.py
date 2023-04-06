import sys
import heapq
input = sys.stdin.readline

V,E = map(int,input().split())
INF = int(1e9)
K = int(input())
adj = [[] for _ in range(V+1)]
for _ in range(V):
    s,e,w = map(int,input().split())
    adj[s].append((e,w))
v = [INF for _ in range(V+1)]
v[K] = 0
def dik(s):
    Q =[]
    heapq.heappush(Q,(0,s))

    while Q:
        cost, current = heapq.heappop(Q)

        if v[current] < cost:
            continue
        for i in adj[current]:
            temp = cost + i[1]
            if v[i[0]] > temp:
                v[i[0]] = temp
                heapq.heappush(Q, (temp, i[0]))
    return

dik(K)

for i in range(1,V+1):
    if v[i] == INF:
        print("INF")
    else:
        print(v[i])
