# O(g(n)) = {f(n)| 모든 n >= n0, f(n) <= c * g(n) 인 c, n0 존재}
# f(n) = a1n + a0
import sys
sys.stdin = open('input.txt')

a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())

if a1 - c > 0:
    print(0)
elif (a1 * n0) + a0 <= c * n0:
    print(1)
else:
    print(0)