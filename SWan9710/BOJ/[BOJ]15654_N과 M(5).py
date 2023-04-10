def DFS(n, lst):
    # 종료조건
    if n == M:
        print(*lst)
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            DFS(n + 1, lst + [arr[i]])
            visited[i] = 0

N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
visited = [0] * N
DFS(0, [])



