import sys
input = sys.stdin.readline
n = int(input())
stack = [0]
count = 0
for _ in range(n):
    x, y = tuple(map(int, input().split()))
    if stack[-1] < y:
        count += 1
        stack.append(y)
    else:
        while stack[-1] > y:
            stack.pop()
        if stack[-1] < y:
            count += 1
            stack.append(y)
print(count)
