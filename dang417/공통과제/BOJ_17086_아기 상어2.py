import sys
sys.stdin = open('input.txt')

from collections import deque
import sys
input = sys.stdin.readline

di = [-1, -1, -1, 0, 0, 1, 1, 1]
dj = [-1, 0, 1, -1, 1, -1, 0, 1]

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
q = deque()
rlt = 0

for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            q.append((i, j))

while q:
    i, j = q.popleft()
    for k in range(8):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < N and 0 <= nj < M:
            if not arr[ni][nj]:
                arr[ni][nj] = arr[i][j] + 1
                q.append((ni, nj))
                rlt = max(rlt, arr[i][j] + 1)

print(rlt - 1)