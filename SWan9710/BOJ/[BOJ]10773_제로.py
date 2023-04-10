N = int(input())
stack = []

for i in range(N):
    num = int(input())
    if num == 0:
        stack.pop()
    else:
        stack.append(num)

if stack:
    print(sum(stack))
else:
    print(0)
