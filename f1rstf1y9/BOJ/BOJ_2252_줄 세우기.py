import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
enter_len = [0]*(N+1)
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    enter_len[b] += 1
    
q = []
for i in range(1,N+1):
    if enter_len[i] == 0:
        q.append(i)
while q:
    p = q.pop()
    print(p, end=' ')
    for i in graph[p]:
        enter_len[i] -= 1
        if enter_len[i] == 0:
            q.append(i)
