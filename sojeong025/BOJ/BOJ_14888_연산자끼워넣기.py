import sys
input = sys.stdin.readline

def dfs(depth, tmp, plus, minus, mul, div):
    global max_num, min_num
    if depth == N:
        max_num = max(tmp, max_num)
        min_num = min(tmp, min_num)
        return
    if plus:
        dfs(depth + 1, tmp + number[depth], plus - 1, minus, mul, div)
    if minus:
        dfs(depth + 1, tmp - number[depth], plus, minus - 1, mul, div)
    if mul:
        dfs(depth + 1, tmp * number[depth], plus, minus, mul - 1, div)
    if div:
        dfs(depth + 1, int(tmp / number[depth]), plus, minus, mul, div - 1)


N = int(input())
number = list(map(int, input().split()))
operator = list(map(int, input().split()))

max_num = -1e9
min_num = 1e9

dfs(1, number[0], operator[0], operator[1], operator[2], operator[3])
print(max_num)
print(min_num)


