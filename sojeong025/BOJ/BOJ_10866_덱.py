from collections import deque
import sys

N = int(sys.stdin.readline())
queue = deque()

for i in range(N):
    name = sys.stdin.readline().split()

    if name[0] == 'push_front':
        queue.appendleft(name[1])
    elif name[0] == 'push_back':
        queue.append(name[1])
    elif name[0] == 'pop_front':
        if queue:
            print(queue[0])
            queue.popleft()
        else:
            print('-1')
    elif name[0] == 'pop_back':
        if queue:
            print(queue[len(queue)-1])
            queue.pop()
        else:
            print('-1')
    elif name[0] == 'size':
        print(len(queue))
    elif name[0] == 'empty':
        if queue:
            print('0')
        else:
            print('1')
    elif name[0] == 'front':
        if queue:
            print(queue[0])
        else:
            print('-1')
    elif name[0] == 'back':
        if queue:
            print(queue[len(queue)-1])
        else:
            print('-1')
