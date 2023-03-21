d = [-1, 0, 1]

def push(x):
    for i in range(3):
        nx = x+d[i]
        if 0 <= nx < N:
            current[nx] = 0 if current[nx] else 1

def solve(n):
    push_cnt = 0
    if n:
        push(0)
        push_cnt = 1
    for i in range(N-1):
        if current[i] != result[i]:
            push(i+1)
            push_cnt += 1
    if current == result:
        return push_cnt
    else:
        return -1

N = int(input())
current = list(map(int, input()))
result = list(map(int, input()))
current_copy = [x for x in current]
a = solve(0)
current = current_copy
b = solve(1)

if a == -1 and b == -1:
    print(-1)
elif a == -1 or b == -1:
    print(max(a, b))
else:
    print(min(a, b))