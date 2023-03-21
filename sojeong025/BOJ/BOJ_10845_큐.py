import sys
N = int(sys.stdin.readline())

queue = []

for _ in range(N):
    name = sys.stdin.readline().split()
    number = name[0]

    if number == 'push':
        result = name[1]
        queue.append(result)

    elif number == 'pop':
        if queue:
            print(queue.pop(0))
        else:
            print(-1)
    
    elif number == 'size':
        print(len(queue))

    elif number == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)

    elif number == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])

    elif number == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])