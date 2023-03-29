import sys
sys.stdin = open('input.txt')

def gcd(A, B):
    while B:
        q = B
        B = A % B
        A = q
    return A

a, b = map(int, input().split())
c, d = map(int, input().split())

x = (a * d) + (c * b)
y = b * d

x, y = x // gcd(x, y), y // gcd(x, y)

print(x, y)