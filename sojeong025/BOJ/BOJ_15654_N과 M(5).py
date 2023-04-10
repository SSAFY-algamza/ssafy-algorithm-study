import sys
sys.stdin = open('input.txt')

def dfs(n, lst):
    if n == M:
        print(' '.join(map(str,lst)))
        return

    for j in range(N):
        if visited[j] == 0:
            visited[j] = 1
            dfs(n+1, lst+[number[j]])
            visited[j] = 0
        
N, M = map(int, input().split())
number = sorted(list(map(int, input().split())))

visited = [0] * N

dfs(0, [])