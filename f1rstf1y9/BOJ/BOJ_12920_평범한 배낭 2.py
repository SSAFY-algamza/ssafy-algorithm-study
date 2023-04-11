# M = 가방의 최대 무게
N, M = map(int, input().split())
things = [(0,0)]
for _ in range(N):
    V, C, K = map(int,input().split())
    i = 1
    while K > 0:
        k = min(i, K)
        things.append((V*k, C*k))
        i *= 2
        K -= k
N = len(things)
dp = [[0]*(M+1) for _ in range(N)]
for i in range(1, N):
    for j in range(M+1):
        if j-things[i][0] >= 0:
            dp[i][j] = max(dp[i-1][j-things[i][0]]+things[i][1], dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]
print(max(dp[N-1]))