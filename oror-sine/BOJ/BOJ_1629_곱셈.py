import sys
A, B, C = map(int, sys.stdin.readline().split())
ans = 1
while B != 0:
    cnt = 1
    tmp = A
    while cnt*2 < B:
        cnt *= 2
        tmp *= tmp
        tmp %= C
    ans *= tmp
    B -= cnt
print(ans % C)
