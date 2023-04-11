for _ in range(3):
    N = int(input())
    coins = []
    total = 0
    for _ in range(N):
        coin, n = map(int, input().split())
        coins.append((coin, n))
        total += coin*n
    if total%2:
        print(0)
        continue
    M = total // 2
    dp = [1] + [0]*M
    #i번쨰 동전까지 확인해서 j 금액을 만들수있는지?
    for i in range(len(coins)):
        c, n = coins[i]
        for j in range(M, c-1, -1):
            if dp[j-c]:
                for k in range(n):
                    if j+c*k < M+1:
                        dp[j+c*k] = 1
                    else:
                        break
    print(dp[M])