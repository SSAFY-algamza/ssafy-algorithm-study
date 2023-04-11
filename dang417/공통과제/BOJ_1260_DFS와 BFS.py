import sys
sys.stdin = open('input.txt')

def DFS(V):
    print(V+1, end=' ')
    for i in range(N):
        if graph[V][i] and not visited[i]:
            visited[i] = 1
            DFS(i)

def BFS(V):
    q = []
    q.append(V)
    while q:
        s = q.pop(0)
        print(s+1, end=' ')
        for i in range(N):
            if graph[s][i] and not visited[i]:
                visited[i] = 1
                q.append(i)

N, M, V = map(int, input().split())
graph = [[0] * N for _ in range(N)]

for _ in range(M):
    i, j = map(int, input().split())
    graph[i-1][j-1] = 1
    graph[j-1][i-1] = 1

visited = [0] * N
visited[V-1] = 1
DFS(V-1)
print()

visited = [0] * N
visited[V-1] = 1
BFS(V-1)
print()
