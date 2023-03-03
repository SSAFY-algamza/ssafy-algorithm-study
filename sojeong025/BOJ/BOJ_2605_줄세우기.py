import sys
sys.stdin = open('input.txt')

student = int(input())
line = [0] * student
num = list(map(int, input().split()))
for i in range(1, student+1):
    line[i-num[i-1]:] = line[i - num[i-1] - 1: -1]
    line[i-num[i-1]-1] = i

print(*line)
