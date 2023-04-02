import sys
from collections import deque

N, M, V = map(int, sys.stdin.readline().split())
dict = {int(i):[] for i in range(1, N+1)}

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    dict[i].append(j)
    dict[j].append(i)

for i in range(1, N+1):
    dict[i].sort()


def dfs(node):
    visited = [False]*(N+1)
    visited[node] = True

    def recursion(node):
        print(node, end=' ')
        for i in dict[node]:
            if not visited[i]:
                visited[i] = True
                recursion(i)

    recursion(node)
    print()


def bfs(node):
    visited = [False]*(N+1)
    visited[node] = True
    queue = deque()
    queue.append(node)

    while queue:
        node = queue.popleft()
        print(node, end=' ')
        for i in dict[node]:
            if not visited[i]: 
                visited[i] = True       
                queue.append(i)
    
    print()

dfs(V)
bfs(V)