import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
number = sorted(list(map(int, input().split())))
lst = []

def dfs():
    if len(lst) == M:
        print(*lst)
        return
    for i in range(N):
        lst.append(number[i])
        dfs()
        lst.pop()

dfs()