delta = [-1,0,1]
X, Y = map(int, input().split())
if Y-X == 1 or Y-X == 0:
    print(Y-X)
else:
    n = 0
    while Y-X > n*(n+1):
        n += 1
    if Y-X <= n*n:
        print(n*2-1)
    else:
        print(n*2)
