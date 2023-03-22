import sys
N = int(sys.stdin.readline())
RGBs = [[int(i) for i in sys.stdin.readline().split()] for _ in range(N)]

ans = []
if N == 2:
    for a in range(3):
        for b in range(3):
            if a != b:
                ans.append(RGBs[0][a] + RGBs[1][b])
else:
    dp = [[[0]*3 for _ in range(N-2)] for _ in range(3)]
    for a in range(3):
        for b in range(3):
            for c in range(3):
                if a != b and b!=c:
                    if dp[a][0][c]:
                        dp[a][0][c] = min(dp[a][0][c], RGBs[0][a] + RGBs[1][b] + RGBs[2][c])
                    else:
                        dp[a][0][c] = RGBs[0][a] + RGBs[1][b] + RGBs[2][c] 
                    
    for a in range(3):
        for i in range(1, N-2):
            dp[a][i][0] = min(dp[a][i-1][1], dp[a][i-1][2]) + RGBs[i+2][0]
            dp[a][i][1] = min(dp[a][i-1][0], dp[a][i-1][2]) + RGBs[i+2][1]
            dp[a][i][2] = min(dp[a][i-1][0], dp[a][i-1][1]) + RGBs[i+2][2]
    for a in range(3):
        for c in range(3):
            if a != c:
                ans.append(dp[a][N-3][c])
print(min(ans))
