import sys
sys.stdin = open('input.txt')

N, K = map(int, input().split())

rlt = []

for i in range(1, N+1):
    if not N % i:
        rlt.append(i)

if len(rlt) < K:
    print(0)

else:
    print(rlt[K-1])
