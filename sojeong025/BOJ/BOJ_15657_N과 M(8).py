import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
number = sorted(list(map(int, input().split())))
lst = []

def dfs(s):
    if len(lst) == M:
        print(*lst)
        return
    for i in range(s, N):
        lst.append(number[i])
        dfs(i)
        lst.pop()

dfs(0)