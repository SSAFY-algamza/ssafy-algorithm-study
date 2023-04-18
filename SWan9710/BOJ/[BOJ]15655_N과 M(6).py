def DFS(n, s, lst):
    if n == M:
        result.append(lst)
        return

    for i in range(s, N):
        if visited[i] == 0:
            visited[i] = 1
            DFS(n + 1, i, lst + [arr[i]])
            visited[i] = 0

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

visited = [0] * N
result = []

DFS(0, 0, [])
for lst in result:
    print(*lst)
