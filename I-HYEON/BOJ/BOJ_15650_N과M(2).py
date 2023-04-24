N,M = map(int,input().split())

def backtrack(depth,chosen):
    if depth == M:
        print(*chosen)
        return

    if chosen:
        start = chosen[-1]+1
    else:
        start = 1
    for i in range(start, N+1):
        if i not in chosen:
            chosen.append(i)
            backtrack(depth+1,chosen)
            chosen.pop()

backtrack(0,[])