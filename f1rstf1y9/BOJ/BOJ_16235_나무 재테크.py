from collections import deque
import sys
input = sys.stdin.readline

delta = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

def year():
    global ground, trees
    temp = deque([])
    for i in range(N):
        for j in range(N):

            while trees[i][j]:
                t = trees[i][j].popleft()
                if ground[i][j] >= t:
                    temp.append((i,j,t+1))
                    ground[i][j] -= t

                    if (t+1) % 5 == 0:
                        for k in range(8):
                            d = delta[k]
                            ni, nj = i+d[0], j+d[1]
                            if 0 <= ni < N and 0 <= nj < N:
                                temp.appendleft((ni,nj,1))
                else:
                    trees[i][j].append(t)
                    break
            while trees[i][j]:
                ground[i][j] += trees[i][j].pop()//2

    while temp:
        x, y, t = temp.pop()
        trees[x][y].appendleft(t)

    for i in range(N):
        for j in range(N):
            ground[i][j] += A[i][j]

N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
ground = [[5]*N for _ in range(N)]
trees = [[deque([]) for _ in range(N)] for _ in range(N)]
for _ in range(M):
    x, y, z = map(int, input().split())
    trees[x-1][y-1].append(z)

for _ in range(K):
    year()

ans = 0
for i in range(N):
    for j in range(N):
       ans += len(trees[i][j])

print(ans)