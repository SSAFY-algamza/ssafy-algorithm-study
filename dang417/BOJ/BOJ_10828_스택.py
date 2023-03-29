import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline
N = int(input())
stack = []
for _ in range(N):
    A = list(input().split())
    oper = A[0]
    if len(A) > 1:
        num = int(A[1])
    if oper == 'push':
        stack.append(num)
    elif oper == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif oper == 'size':
        print(len(stack))
    elif oper == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    elif oper == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)