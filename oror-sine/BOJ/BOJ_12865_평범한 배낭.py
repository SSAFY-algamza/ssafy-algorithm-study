import sys

N, K = map(int, sys.stdin.readline().split())
items = [(0, 0)]
for _ in range(N):
    items.append(tuple(int(i) for i in sys.stdin.readline().split()))

dp = [[0] * (K + 1) for _ in range(N + 1)]
for n in range(1, N + 1):
    for k in range(1, K + 1):
        w, v = items[n]
        if k < w:
            dp[n][k] = dp[n - 1][k]
        else:
            dp[n][k] = max(dp[n - 1][k], dp[n - 1][k - w] + v)
print(dp[N][K])
