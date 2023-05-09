X, A, B, C, D = map(int, input().split())
total = A+B*5+C*10+D*25
dp = [[0,0,0,0] for _ in range(total+1)]
dp[total] = [A,B,C,D]
n = total-1
if X > total:
    print(0,0,0,0)
elif X == total:
    print(A,B,C,D)
else:
    while n >= X:
        max_cnt = 0
        max_value = [0,0,0,0]
        if n+1 <= total:
            a,b,c,d = dp[n+1]
            if a and sum([a-1,b,c,d]) >= max_cnt:
                max_cnt = sum([a-1,b,c,d])
                max_value = [a-1,b,c,d]
        if n+5 <= total:
            a, b, c, d = dp[n+5]
            if b and sum([a, b-1, c, d]) >= max_cnt:
                max_cnt = sum([a, b-1, c, d])
                max_value = [a,b-1,c,d]
        if n+10 <= total:
            a,b,c,d = dp[n+10]
            if c and sum([a,b,c-1,d]) >= max_cnt:
                max_cnt = sum([a,b,c-1,d])
                max_value = [a,b,c-1,d]
        if n+25 <= total:
            a, b, c, d = dp[n+25]
            if d and sum([a, b, c, d-1]) >= max_cnt:
                max_cnt = sum([a, b, c, d-1])
                max_value = [a,b,c,d-1]
        dp[n] = max_value
        n -= 1
    print(*dp[X])