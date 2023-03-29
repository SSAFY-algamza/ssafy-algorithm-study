N,M = map(int,input().split())

def backtrack(depth,chosen):
    if depth == M:
        print(*chosen)
        return

    for i in range(1, N+1):
        chosen.append(i)
        backtrack(depth+1,chosen)
        chosen.pop()

backtrack(0,[])