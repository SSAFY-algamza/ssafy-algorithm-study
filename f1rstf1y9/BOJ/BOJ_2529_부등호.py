def bt(n): #선택된 숫자의 수
    global min_v, max_v
    if n == k+1:
        res = int(''.join(stack))
        min_v = min(res, min_v)
        max_v = max(res, max_v)
        return
    for i in range(10):
        if str(i) not in stack:
            if n == 0 \
                or (op[n-1] == '<' and int(stack[-1]) < i)\
                or (op[n-1] == '>' and int(stack[-1]) > i):
                    stack.append(str(i))
                    bt(n+1)
                    stack.pop()

k = int(input())
op = input().split()
visited = [0]*10
min_v = int('9'*(k+1))
max_v = 0
stack = []
bt(0)
print(max_v)
print(str(min_v).zfill(k+1))