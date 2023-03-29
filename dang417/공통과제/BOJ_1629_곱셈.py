import sys
sys.stdin = open('input.txt')

def mult(A, B):
    if B == 1:
        return A % C

    tmp = mult(A, B//2)

    if B % 2:
        return tmp * tmp * A % C
    else:
        return tmp * tmp % C

A, B, C = map(int, input().split())

print(mult(A, B))