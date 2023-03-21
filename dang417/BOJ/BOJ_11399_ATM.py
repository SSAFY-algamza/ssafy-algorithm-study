import sys
sys.stdin = open('input.txt')

N = int(input())
P = sorted(list(map(int, input().split())))
prefix_sum = [0] * N

for i in range(N):
    prefix_sum[i] = prefix_sum[i-1] + P[i]

print(sum(prefix_sum))