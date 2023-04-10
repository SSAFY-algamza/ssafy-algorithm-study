import sys
sys.stdin = open('input.txt')

def dfs(n, start, lst):
    if n == M:
        print(' '.join(map(str,lst)))
        return

    for j in range(start, N+1):
        dfs(n+1, j, lst+[j])
        
N, M = map(int, input().split())
dfs(0, 1, [])