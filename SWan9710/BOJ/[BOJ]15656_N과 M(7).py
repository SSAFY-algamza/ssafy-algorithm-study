def DFS(n, lst):
    if n == M:
        result.append(lst)
        return

    for i in range(N):
        DFS(n + 1, lst + [arr[i]])

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

result = []

DFS(0, [])
for lst in result:
    print(*lst)
