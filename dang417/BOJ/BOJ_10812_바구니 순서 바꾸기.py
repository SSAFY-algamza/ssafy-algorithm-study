import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
baskets = list(range(1, N+1))

for _ in range(M):
    stack_left = []
    stack_right = []
    i, j, k = map(int, input().split())
    for _ in range(k-i):
        stack_left.append(baskets.pop(i-1))

    for _ in range(N-j):
        stack_right.append(baskets.pop())

    baskets += stack_left
    baskets += stack_right[::-1]

print(*baskets)