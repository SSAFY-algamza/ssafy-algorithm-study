import sys
sys.stdin = open('input.txt')

import sys
from collections import deque

t = int(input())

for i in range(t):
    p = sys.stdin.readline().rstrip()
    n = int(input())
    num = sys.stdin.readline().rstrip()[1:-1].split(",")
    num = deque(num)

    R = 0

    if not n:
        num = []

    for j in p:
        if j == 'R':
            R += 1
        elif j == 'D':
            if len(num) < 1:
                print("error")
                break
            else:
                if R % 2:
                    num.pop()
                else:
                    num.popleft()
    else:
        if R % 2 == 0:
            print("[" + ",".join(num) + "]")
        else:
            num.reverse()
            print("[" + ",".join(num) + "]")