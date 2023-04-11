N = int(input())
weight = [0]+list(map(int, input().split()))
K = int(input())
M = sum(weight)
# dp[i][w] i번째 무게추까지 확인했을때 w 무게 확인하는데 사용되는 최소개수
dp = [[31]*(M+1) for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(M+1):
        if weight[i] == j:
            dp[i][j] = 1
        elif j-weight[i] >= 0:
            dp[i][j] = min(dp[i-1][j], dp[i-1][j-weight[i]]+1)
        else:
            dp[i][j] = dp[i-1][j]
valid = []
for i in range(M+1):
    if dp[N][i] != 31:
        valid.append(i)
for c in map(int, input().split()):
    if c >= M+1:
        print('N', end=' ')
        continue
    if dp[N][c] != 31:
        print('Y', end=' ')
        continue
    for v in valid:
        if c+v < M+1 and dp[N][c+v] != 31:
            print('Y', end=' ')
            break
    else:
        print('N', end=' ')