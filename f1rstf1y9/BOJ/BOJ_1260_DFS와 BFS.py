from collections import deque
def dfs(n):
    print(n, end=' ')
    if not graph[n]:
        return
    for i in sorted(graph[n]):
        if not dfs_visited[i]:
            dfs_visited[i] = 1
            dfs(i)

def bfs(n):
    q = deque([n])
    while q:
        n = q.popleft()
        print(n, end=' ')
        if not graph[n]:
            return
        for i in sorted(graph[n]):
            if not bfs_visited[i]:
                bfs_visited[i] = 1
                q.append(i)

N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs_visited = [0]*(N+1)
dfs_visited[V] = 1
dfs(V)
print()
bfs_visited = [0]*(N+1)
bfs_visited[V] = 1
bfs(V)
