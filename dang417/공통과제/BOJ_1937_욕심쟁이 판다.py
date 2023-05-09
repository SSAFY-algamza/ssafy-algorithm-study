import sys
sys.stdin = open('input.txt')

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def DFS(i, j):
    if not DP[i][j]:
        DP[i][j] = 1
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < N:
                if forest[ni][nj] > forest[i][j]:
                    DP[i][j] = max(DP[i][j], DFS(ni, nj))

    return DP[i][j] + 1

N = int(input())
forest = [list(map(int, input().rstrip().split())) for _ in range(N)]
DP = [[0] * N for _ in range(N)]
rlt = 0

for i in range(N):
    for j in range(N):
        rlt = max(rlt, DFS(i, j))

print(rlt-1)