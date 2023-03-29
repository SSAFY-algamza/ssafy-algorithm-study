def bt(value, idx):
    global plus,minus,mul,div,min_v,max_v

    if idx == N:
        max_v = max(value, max_v)
        min_v = min(value, min_v)
        return
    if plus:
        plus -= 1
        bt(value + A[idx], idx+1)
        plus += 1
    if minus:
        minus -= 1
        bt(value - A[idx], idx+1)
        minus += 1
    if mul:
        mul -= 1
        bt(value * A[idx], idx+1)
        mul += 1

    if div:
        div -= 1
        bt(int(value / A[idx]), idx+1)
        div += 1

N = int(input())
A = list(map(int, input().split()))
plus,minus,mul,div = map(int, input().split())

visited = [0]*(N-1)
min_v = 1e22
max_v = -1e22
bt(A[0], 1)
print(max_v)
print(min_v)
