N,M = map(int,input().split())
ans = []

def backtrack(depth,chosen):
    if depth == M:
        print(*chosen)
        return
    
    for i in range(1, N+1):
        chosen.append(i)
        if len(chosen) <=1 or chosen[-2] <= chosen[-1]:  # 방금 담은 숫자가 그 전에 담은 숫자보다 크거나 같을 때만
            backtrack(depth+1,chosen)  # 계속 탐색한다.
        chosen.pop()

backtrack(0,[])
for i in range(len(ans)):
    print(*ans[i])