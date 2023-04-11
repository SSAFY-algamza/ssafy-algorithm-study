T = int(input())
for _ in range(T):
    N = int(input())
    coin = list(map(int, input().split()))
    M = int(input())
    dp = [[0]*(M+1) for _ in range(N+1)]
    for i in range(1,N+1):
        for j in range(M+1):
            if coin[i-1] == j:
                dp[i][j] = 1
            if j-coin[i-1] >= 0:
                dp[i][j] += dp[i-1][j]+dp[i][j-coin[i-1]]
            else:
                dp[i][j] += dp[i-1][j]
    print(dp[N][M])
