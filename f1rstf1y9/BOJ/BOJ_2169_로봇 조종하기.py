N, M = map(int,input().split())
mars = [list(map(int, input().split())) for _ in range(N)]

# 같은 줄에서 왼쪽으로만 이동
dp_left = [[0]*M for _ in range(N)]
# 같은 줄에서 오른쪽으로만 이동
dp_right = [[0]*M for _ in range(N)]
# 왼쪽이동, 오른쪽 이동 비교해서 둘 중 최대 가치를 저장할 리스트
dp = [[0]*M for _ in range(N)]

dp[0][0] = mars[0][0]
for i in range(1, M):
    dp[0][i] = dp[0][i-1]+mars[0][i]

for i in range(1, N):
    dp_right[i][0] = dp[i-1][0]+mars[i][0]
    dp_left[i][M-1] = dp[i-1][M-1]+mars[i][M-1]
    for j in range(1, M):
        dp_right[i][j] = max(dp[i-1][j], dp_right[i][j-1])+mars[i][j]
    for j in range(M-2, -1, -1):
        dp_left[i][j] = max(dp[i-1][j], dp_left[i][j+1])+mars[i][j]
    for j in range(M):
        dp[i][j] = max(dp_right[i][j], dp_left[i][j])

print(dp[N-1][M-1])