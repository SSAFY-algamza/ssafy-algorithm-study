import sys
sys.stdin = open('input.txt')

import sys
from collections import deque

input = sys.stdin.readline

di = [0, 0, -1, 1]
dj = [-1, 1, 0, 0]

def melt():
    melt_data = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if data_arr[i][j]:
                for k in range(4):
                    ni = i + di[k]
                    nj = j + dj[k]
                    if 0 <= ni < N and 0 <= nj < M:
                        if not data_arr[ni][nj]:
                            melt_data[i][j] += 1
    for i in range(N):
        for j in range(M):
            if data_arr[i][j] - melt_data[i][j] < 0:
                data_arr[i][j] = 0
            elif data_arr[i][j]:
                data_arr[i][j] -= melt_data[i][j]

def BFS(start):
    q = deque()
    q.append(start)
    visited[start[0]][start[1]] = 1
    while q:
        i, j = q.popleft()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < M:
                if data_arr[ni][nj] and not visited[ni][nj]:
                    q.append((ni, nj))
                    visited[ni][nj] = 1

N, M = map(int, input().rstrip().split())

data_arr = [list(map(int, input().rstrip().split())) for _ in range(N)]

rlt = 0
while True:
    visited = [[0] * M for _ in range(N)]
    tmp = 0
    for i in range(N):
        for j in range(M):
            if data_arr[i][j] and not visited[i][j]:
                BFS((i, j))
                tmp += 1
    if tmp > 1:
        print(rlt)
        exit()

    for i in range(N):
        if any(data_arr[i]):
            break
    else:
        print(0)
        exit()

    melt()
    rlt += 1