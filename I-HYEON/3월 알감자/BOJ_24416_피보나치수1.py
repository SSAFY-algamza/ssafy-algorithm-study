def r_fibo(n):  # 재귀로 만든 피보나치 함수
    global ans1
    if n == 1 or n == 2:
        return 1
    else:
        ans1 += 1
        return r_fibo(n - 1) + r_fibo(n - 2)


def dp_fibo(n):  # dp로 만든 피보나치 함수
    global ans2
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 1
    for i in range(3, n + 1):
        ans2 += 1
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


N = int(input())
ans1 = 1
ans2 = 0

r_fibo(N)
dp_fibo(N)

print(ans1,ans2)