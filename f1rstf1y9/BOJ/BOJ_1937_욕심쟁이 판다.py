import sys
sys.setrecursionlimit(10**5)

n = int(input())
forest = [list(map(int, input().split())) for _ in range(n)]
delta = [(-1,0),(1,0),(0,-1),(0,1)]

dp = [[-1]*n for _ in range(n)]
def dfs(x,y):
    if dp[x][y] != -1:
        return dp[x][y]
    dp[x][y] = 1
    for dx, dy in delta:
        nx, ny = x+dx, y+dy
        if 0 <= nx < n and 0 <= ny < n:
            if forest[nx][ny] > forest[x][y]:
                dp[x][y] = max(dp[x][y], dfs(nx, ny)+1)
    return dp[x][y]

ans = 1
for i in range(n):
    for j in range(n):
        ans = max(ans, dfs(i,j))
print(ans)
