import sys
input = sys.stdin.readline
N, M = map(int,input().split())
weapons = [list(map(int, input().split())) for _ in range(N)]
# dp[i][j] -> i회차에서  j무기를 선택했을 때 i회차까지의 총 클리어 시간 최솟값
dp = weapons[0][:]
for i in range(1, N):
    temp = [10001]*M
    for j in range(M):
        temp[j] = min(dp[:j]+dp[j+1:])+weapons[i][j]
    dp = temp
print(min(dp))