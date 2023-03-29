def dfs(k, cnt):
    if graph[k]:
        for i in graph[k]:
            if i == b:
                return cnt+1
            if not visited[i]:
                visited[i] = 1
                res = dfs(i, cnt+1)
                if res != -1:
                    return res
                visited[i] = 0
    return -1

n = int(input())
a, b = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [0]*(n+1)
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited[a] = 1
print(dfs(a, 0))