import sys
sys.stdin = open('input.txt')

def dfs(n, lst):
    if n == M:
        print(' '.join(map(str,lst)))
        return

    for j in range(1, N+1):
        dfs(n+1, lst+[j])
        
N, M = map(int, input().split())
ans = []
dfs(0, [])
