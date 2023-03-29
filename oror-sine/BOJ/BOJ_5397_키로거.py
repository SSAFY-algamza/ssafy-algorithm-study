import sys

T = int(sys.stdin.readline())
for _ in range(T):
    keys = sys.stdin.readline().rstrip()
    front = []
    rear = []
    for key in keys:
        if key == "<":
            if front:
                rear.append(front.pop())
            continue
        if key == ">":
            if rear:
                front.append(rear.pop())
            continue
        if key == "-":
            if front:
                front.pop()
            continue
        front.append(key)
    print("".join(front + rear[::-1]))
