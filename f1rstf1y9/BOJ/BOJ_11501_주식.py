T = int(input())
for _ in range(T):
    N = int(input())
    stock = list(map(int, input().split()))[::-1]
    high = stock[0]
    cost = 0
    for i in range(1, len(stock)):
        if high >= stock[i]:
            cost += (high-stock[i])
        else:
            high = stock[i]
    print(cost)
