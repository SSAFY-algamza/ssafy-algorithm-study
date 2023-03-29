import sys

N = int(input())
stack = []

for i in range(N):
    word = sys.stdin.readline().strip()
    if len(word) >= 6:
        stack.append(int(word[5:]))
    elif word == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif word =='size':
        print(len(stack))
    elif word == 'empty':
        if not stack:
            print(1)
        else:
            print(0)
    else:
        if stack:
            print(stack[-1])
        else:
            print(-1)





