import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

t = int(input())

for tc in range(t):
    stack = []
    string = input().rstrip()
    for char in string:
        if char == "(":
            stack.append(char)
        elif char == ")":
            if stack:
                stack.pop()
            else:
                print('NO')
                break
    else:
        if stack:
            print('NO')
        else:
            print('YES')