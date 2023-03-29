import sys
sys.stdin = open('input.txt')

N = int(input())

idx = [list(map(int, input().split())) for _ in range(N)]

x_max = max(idx, key=lambda x : x[0])[0]
x_min = min(idx, key=lambda x : x[0])[0]
y_max = max(idx, key=lambda x : x[1])[1]
y_min = min(idx, key=lambda x : x[1])[1]

print((x_max-x_min)*(y_max-y_min))

