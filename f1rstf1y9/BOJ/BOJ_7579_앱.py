N, M = map(int, input().split())
# 메모리 - N개
memory = list(map(int, input().split()))
# 비용 - N개
cost = list(map(int, input().split()))
# 최대 비용
K = sum(cost)

# dp[i,c] = i번째 앱까지 확인했을때, 비용한도 c일때 확보할 수 있는 메모리
dp = [[0]*(K+1) for _ in range(N+1)]
min_cost = K+1
for i in range(1, N+1):
    for j in range(K+1): # 비용
        if j-cost[i-1] >= 0: #현재 비용보다 N번째 앱 지우는데 드는 비용이 작거나 같을때
            # i-1개 앱 종료 & 현재 비용에서 N번째 앱 지우는데 드는 비용을 뺀값이 비용한도일때 확보 가능한 메모리 + N번째 앱 지우는데 드는 비용
            # vs i-1개 앱 종료 & 현재 비용이 비용한도일때 확보 가능한 메모리
            dp[i][j] = max(dp[i-1][j-cost[i-1]]+memory[i-1], dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]
        if dp[i][j] >= M:
            min_cost = min(min_cost, j)

print(min_cost)
