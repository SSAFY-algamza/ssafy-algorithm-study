import sys

N = int(sys.stdin.readline())
sequence = [int(i) for i in sys.stdin.readline().split()]
operators = [int(i) for i in sys.stdin.readline().split()]


def calculate(a, b, operator):
    if operator == 0:
        return a + b
    if operator == 1:
        return a - b
    if operator == 2:
        return a * b
    if operator == 3:
        if a < 0:
            return -((-a) // b)
        return a // b


maxi = -1e9
mini = 1e9


def backtrack(idx, result, operators):
    if idx == N:
        global maxi, mini
        if maxi < result:
            maxi = result
        if mini > result:
            mini = result

    for operator in range(4):
        if operators[operator]:
            operators[operator] -= 1
            backtrack(idx + 1, calculate(result, sequence[idx], operator), operators)
            operators[operator] += 1


backtrack(1, sequence[0], operators)
print(maxi)
print(mini)
