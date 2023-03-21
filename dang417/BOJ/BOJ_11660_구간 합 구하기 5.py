import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())

A = [[0] * (N+1)] + [[0] + list(map(int, input().split())) for _ in range(N)]
pre_sum = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(1, N+1):
    for j in range(1, N+1):
        pre_sum[i][j] = A[i][j] + pre_sum[i-1][j] + pre_sum[i][j-1] - pre_sum[i-1][j-1]

for _ in range(M):
    y1, x1, y2, x2 = map(int, input().split())
    print(pre_sum[y2][x2] - pre_sum[y1-1][x2] - pre_sum[y2][x1-1] + pre_sum[y1-1][x1-1])