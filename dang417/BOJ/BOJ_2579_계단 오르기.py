import sys
sys.stdin = open('input.txt')

n = int(input())
dp = [0] * n
stair = [int(input()) for _ in range(n)]

if n <= 2:
    print(sum(stair))
    exit()

dp[0] = stair[0]
dp[1] = dp[0] + stair[1]

for i in range(2, n):
    dp[i] = max(dp[i-3] + stair[i-1] + stair[i], dp[i-2] + stair[i])

print(dp[-1])