def DFS(n, s, lst):
    if n == M:
        print(*lst)
        return

    for i in range(s, N+1):
        DFS(n + 1, i, lst + [i])

N, M = map(int, input().split())
result = []

DFS(0, 1, [])
