import sys
N = int(sys.stdin.readline())

stack = []

for _ in range(N):
    name = sys.stdin.readline().split()
    number = name[0]

    if number == 'push':
        result = name[1]
        stack.append(result)

    elif number == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    
    elif number == 'size':
        print(len(stack))

    elif number == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)

    elif number == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])