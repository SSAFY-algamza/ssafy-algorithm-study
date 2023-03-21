import sys
sys.stdin=open('input.txt')

N = int(input())
number = list(map(int, input().split()))

answer = []
temp = []

def backtracking(x):
    if x == N:
        answer.append(sum(abs(number[temp[i+1]] - number[temp[i]]) for i in range(N-1)))
        return

    for i in range(N):
        if i not in temp:
            temp.append(i)
            backtracking(x+1)
            temp.pop()

backtracking(0)
print(max(answer))
