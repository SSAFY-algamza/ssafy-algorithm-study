import sys

N = int(sys.stdin.readline())
operators = sys.stdin.readline().split()
maxi = [0]*(N+1)
mini = [9]*(N+1)


def backtrack(depth, lst):
    if depth == N:
        global maxi, mini
        maxi = max(maxi, [i for i in lst])
        mini = min(mini, [i for i in lst])
        return
    for i in range(10):
        if visited[i]:
            continue
        if (operators[depth] == ">" and lst[depth] > i) or (operators[depth] == "<" and lst[depth] < i):
            visited[i] = True
            lst[depth+1] = i
            backtrack(depth+1, lst)
            visited[i] = False
            
            
for i in range(10):
    visited = [False]*10
    visited[i] = True
    lst = [0]*(N+1)
    lst[0] = i
    backtrack(0, lst)

print(''.join(map(str, maxi)))
print(''.join(map(str, mini)))