import sys
sys.stdin = open('input.txt')

from collections import deque

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def Dijkstra():
    global D

    q = deque()
    q.append((0, 0))

    while q:
        i, j = q.popleft()

        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < N:

                if D[ni][nj] == 1e9 or D[ni][nj] > D[i][j] + cave[ni][nj]:
                    D[ni][nj] = D[i][j] + cave[ni][nj]
                    q.append((ni, nj))

    return D[N-1][N-1]

    pass

N = int(input())
tc = 0

while N:
    tc += 1
    cave = [list(map(int, input().split())) for _ in range(N)]
    D = [[1e9] * N for _ in range(N)]
    D[0][0] = cave[0][0]
    rlt = Dijkstra()
    print(f'Problem {tc}:', rlt)

    N = int(input())
