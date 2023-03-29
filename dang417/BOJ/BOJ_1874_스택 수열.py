import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

n = int(input())
num = 1
stack = []
rlt = ''

for _ in range(n):
    a = int(input())
    while True:
        if stack and stack[-1] == a:
            stack.pop()
            rlt += '-'
            break
        elif a >= num:
            stack.append(num)
            num += 1
            rlt += '+'
        else:
            print('NO')
            exit()

for i in range(len(rlt)):
    print(rlt[i])