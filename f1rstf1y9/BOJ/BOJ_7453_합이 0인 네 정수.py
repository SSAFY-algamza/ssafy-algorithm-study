import sys
input = sys.stdin.readline

n = int(input())
A = []
B = []
C = []
D = []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

ab = {}
for i in A:
    for j in B:
        ab[i+j] = ab.get(i+j, 0) + 1 # 딕셔너리 키값 없으면 0

ans = 0
for i in C:
    for j in D:
        ans += ab.get(-i-j, 0)
print(ans)