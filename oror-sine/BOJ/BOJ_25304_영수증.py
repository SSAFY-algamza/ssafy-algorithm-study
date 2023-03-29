import sys
total = int(sys.stdin.readline())
N = int(sys.stdin.readline())
prices = 0
for _ in range(N):
    price, cnt = map(int, sys.stdin.readline().split())
    prices += price * cnt
print('Yes' if total == prices else 'No')
