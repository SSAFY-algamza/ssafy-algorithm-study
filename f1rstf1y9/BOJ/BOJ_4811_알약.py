import sys
input = sys.stdin.readline
dp = [0, 1]
while True:
    N = int(input())
    if not N:
        break
    dp = [1] + [0]*N
    for i in range(1, N+1):
        val = 0
        for j in range(i):
            val += dp[j]*dp[i-1-j]
        dp[i] = val
    print(dp[N])
