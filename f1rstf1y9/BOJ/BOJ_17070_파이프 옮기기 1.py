N = int(input())
house = [list(map(int, input().split())) for _ in range(N)]
v_dp = [[0]*N for _ in range(N)]
h_dp = [[0]*N for _ in range(N)]
d_dp = [[0]*N for _ in range(N)]

v_dp[0][1] = 1
for i in range(N):
    for j in range(N):
        # 가로 확인
        if j >= 1 and not house[i][j]:
            v_dp[i][j] = max(v_dp[i][j], v_dp[i][j-1] + d_dp[i][j-1])
        # 세로 확인
        if i >= 1 and not house[i][j]:
            h_dp[i][j] = max(h_dp[i][j], h_dp[i-1][j] + d_dp[i-1][j])
        # 대각선 확인
        if i >= 1 and j >= 1 and not (house[i][j] or house[i-1][j] or house[i][j-1]):
            d_dp[i][j] = max(d_dp[i][j],v_dp[i-1][j-1] + h_dp[i-1][j-1] + d_dp[i-1][j-1])

print(v_dp[N-1][N-1] + h_dp[N-1][N-1] + d_dp[N-1][N-1])