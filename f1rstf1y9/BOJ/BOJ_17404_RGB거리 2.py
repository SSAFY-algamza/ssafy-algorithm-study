N = int(input())
cost = [list(map(int, input().split())) for _ in range(N)]
dp = [[0]*3 for _ in range(N+1)]

# 첫번째 집 색 i, 마지막 집 색 j
ans = 1e9
for i in range(3):
    for j in range(3):
        if j != i:
            dp[1][j] = 1e9
        else:
            dp[1][j] = cost[0][i]
    for j in range(2, N+1):
       dp[j][0] = min(dp[j-1][1], dp[j-1][2])+cost[j-1][0]
       dp[j][1] = min(dp[j-1][0], dp[j-1][2])+cost[j-1][1]
       dp[j][2] = min(dp[j-1][1], dp[j-1][0])+cost[j-1][2]
    for j in range(3):
        if j != i:
            ans = min(ans, dp[N][j])
print(ans)
