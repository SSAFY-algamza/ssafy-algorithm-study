import sys
N = int(sys.stdin.readline())
RGBs = [[int(i) for i in sys.stdin.readline().split()] for _ in range(N)]
dp = [[0]*3 for _ in range(N)]
dp[0] = RGBs[0]
for i in range(1, N):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + RGBs[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + RGBs[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + RGBs[i][2]
print(min(dp[-1]))
