from collections import deque

dy = [-1, 0, 0, 1]
dx = [0, -1, 1, 0]

def bfs(y,x):
    q = deque([(1,y,x)])
    eadible = []
    while q:
        t, y, x = q.popleft()
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx]:
                visited[ny][nx] = 1
                if space[ny][nx] <= baby_size:
                    if space[ny][nx] and space[ny][nx] < baby_size:
                        eadible.append((t,ny,nx))
                    q.append((t+1,ny,nx))
    if not eadible:
        return None
    eadible.sort(key=lambda x:(x[0],x[1],x[2]))
    shark = eadible[0]
    return shark[0], shark[1], shark[2]

N = int(input())
space = [list(map(int, input().split())) for _ in range(N)]
fish = 0
for i in range(N):
    for j in range(N):
        if space[i][j] in [1,2,3,4,5,6]:
            fish += 1
        if space[i][j] == 9:
            space[i][j] = 0
            by, bx = i, j

baby_size, eat = 2, 0
second = 0
while fish:
    visited = [[0] * N for _ in range(N)]
    visited[by][bx] = 1
    res = bfs(by, bx)
    if res:
        t, by, bx = res
    else:
        break
    space[by][bx] = 0
    second += t
    fish -= 1
    if eat+1 == baby_size:
        eat = 0
        baby_size += 1
    else:
        eat += 1
print(second)