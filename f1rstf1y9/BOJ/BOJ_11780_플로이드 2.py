n = int(input())
m = int(input())

INF = int(1e9)
graph = [[INF]*(n+1) for _ in range(n+1)]
way = [[[]]*(n+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            graph[i][j] = 0
            way[i][j] = []
        else:
            way[i][j] = [i,j]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = min(graph[a][b],c)

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            if graph[a][b] > graph[a][k] + graph[k][b]:
                graph[a][b] = graph[a][k] + graph[k][b]
                way[a][b] = way[a][k]+way[k][b][1:]

for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print(0, end=" ")
        else:
            print(graph[a][b], end=" ")
    print()

for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print(0)
        else:
            print(len(way[a][b]), *way[a][b])

