import sys
sys.stdin = open('input.txt')

def gcd(A, B):
    while B:
        q = B
        B = A % B
        A = q
    return A

A, B = map(int, input().split())

print(A*B//gcd(A, B))