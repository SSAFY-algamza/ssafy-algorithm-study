import sys
sys.stdin = open('input.txt')

N, K = map(int, input().split())
coins = list(int(input()) for _ in range(N))
rlt = 0

for i in range(N-1, -1, -1):
    if coins[i] <= K:
        cnt = K // coins[i]
        if K % coins[i]:
            rlt += cnt
            K -= coins[i] * cnt
        else:
            rlt += cnt
            break

print(rlt)