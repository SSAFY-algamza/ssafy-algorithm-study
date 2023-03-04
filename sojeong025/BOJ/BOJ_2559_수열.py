import sys
sys.stdin = open('input.txt')

N, K = map(int, input().split())
temperature = list(map(int, input().split()))

temp = []
temp.append(sum(temperature[:K]))
for i in range(N-K):
    temp.append(temp[i] - temperature[i] + temperature[K+i])
print(max(temp))


