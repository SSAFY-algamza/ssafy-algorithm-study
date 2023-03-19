import sys
a, b, c = map(int, sys.stdin.readline().split())
if a == b == c:
    print(10_000+1_000*a)
elif (n := a) == b or (n := b) == c or (n := c) == a:
    print(1_000+100*n)
else:
    print(100*max(a, b, c))
