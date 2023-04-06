import sys

X = int(sys.stdin.readline())
sticks = [64]
total = 64
while X < total:
    sticks[-1] //= 2
    if X <= total - sticks[-1]:
        total -= sticks[-1]
    else:
        sticks.append(sticks[-1])
print(len(sticks))