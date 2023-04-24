import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

T = int(input())
for i in range(T):
    stack = []
    string = input()
    for j in string:
        if j =='(':
            stack.append(j)
        elif j == ')':
            if stack:
                stack.pop()
            else:
                print("NO")
                break
    else:
        if not stack:
            print("YES")
        else:
            print("NO")