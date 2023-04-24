import sys
input = sys.stdin.readline

N, M = map(int, input().split())
number = sorted(list(map(int, input().split())))
lst = []

def dfs(s):
    if len(lst) == M:
        print(*lst)
        return
    for i in range(s, N):
        if number[i] not in lst:
            lst.append(number[i])
            dfs(i + 1)
            lst.pop()

dfs(0)