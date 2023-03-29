import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline
K = int(input())
stack = []

for _ in range(K):
    num = int(input())
    if num:
        stack.append(num)
    else:
        stack.pop()

print(sum(stack))