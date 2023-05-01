import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def bt(n, cur): # 현재 확인한 멤버수, 현재 능력치 합
    global ans
    if n == 11:
        ans = max(ans, cur)
        return
    for i in range(11):
        if S[n][i] and not visited[i]:
            visited[i] = 1
            bt(n+1, cur+S[n][i])
            visited[i] = 0


C = int(input())
for _ in range(C):
    S = [list(map(int, input().split())) for _ in range(11)]
    ans = 0
    visited = [0]*11
    bt(0, 0)
    print(ans)