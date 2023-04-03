import sys

N = int(sys.stdin.readline())
seq = [int(i) for i in sys.stdin.readline().split()]

dp_front = [1]*N
dp_rear = [1]*N

for i in range(N):
    for j in range(i):
        if seq[i] > seq[j]:
            dp_front[i] = max(dp_front[i], dp_front[j]+1)
        if seq[-(i+1)] > seq[-(j+1)]:
            dp_rear[-(i+1)] = max(dp_rear[-(i+1)], dp_rear[-(j+1)]+1)

maxi = 0
for i in range(N):
    length = dp_front[i] + dp_rear[i] - 1
    if maxi < length:
        maxi = length
        
print(maxi)
