from collections import deque

def bfs(node):
    queue = deque()
    queue.append(node)
    while queue:
        node = queue.popleft()
        for n in graph[node]:
            if check[n] == 0:
                check[n] = check[node]+1
                queue.append(n)
            
n = int(input())
graph = [[] for _ in range(n+1)]
a, b = map(int, input().split())

# 연결 관계 초기화
for _ in range(int(input())):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
check = [0]*(n+1)

bfs(a)
print(check[b] if check[b] > 0 else -1)