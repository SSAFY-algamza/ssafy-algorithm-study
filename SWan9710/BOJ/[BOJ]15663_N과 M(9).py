def DFS(n, lst):
    if n == M:
        result.append(lst)
        return
    num = 0
    for i in range(N):
        if visited[i] == 0 and num != arr[i]:
            num = arr[i]
            visited[i] = 1
            DFS(n + 1, lst+[arr[i]])
            visited[i] = 0

N, M = map(int, input().split())
arr = list(map(int, input().split()))
result = []
arr.sort()

visited = [0] * N

DFS(0, [])

for lst in result:
    print(*lst)