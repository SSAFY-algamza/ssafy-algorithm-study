import sys
N, K = map(int, sys.stdin.readline().split())
kits = [int(i)-K for i in sys.stdin.readline().split()]
did = [False]*N
ans = 0
def backtrack(depth, w):
    if depth == N:
        global ans
        ans += 1
    for i in range(N):
        if not did[i] and (nw:=w+kits[i]) >= 500:
            did[i] =True
            backtrack(depth+1, nw)
            did[i] =False

backtrack(0, 500)
print(ans)