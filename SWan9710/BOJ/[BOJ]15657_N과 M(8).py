def DFS(n, s, lst):
    if n == M:
        result.append(lst)
        return

    for i in range(s, N):
        DFS(n + 1, i, lst + [arr[i]])

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

result = []

DFS(0, 0, [])
for lst in result:
    print(*lst)
