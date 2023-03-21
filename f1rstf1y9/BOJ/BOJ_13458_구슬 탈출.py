from collections import deque

delta = [(-1,0), (1,0), (0,-1), (0,1)]

def tilt(x, y, d):
    cnt = 0
    while board[x+d[0]][y+d[1]] != '#' and board[x][y] != 'O':
        x, y = x+d[0], y+d[1]
        cnt += 1
    return x, y, cnt

def bfs(rx, ry, bx, by, cnt):
    q = deque([(rx, ry, bx, by, cnt)])
    while q:
        rx, ry, bx, by, cnt = q.popleft()
        if cnt >= 10:
            return 0
        for i in range(4):
            d = delta[i]
            nrx, nry, rcnt = tilt(rx, ry, d)
            nbx, nby, bcnt = tilt(bx, by, d)

            if board[nbx][nby] == 'O':
                continue

            if board[nrx][nry] == 'O':
                return 1

            if (nrx, nry) == (nbx, nby):
                if rcnt > bcnt: # 빨간색이 더 많이 이동 (빨간색이 뒤)
                    nrx, nry = nrx-d[0], nry-d[1]
                else:
                    nbx, nby = nrx - d[0], nry - d[1]

            if not visited[nrx][nry][nbx][nby]:
                visited[nrx][nry][nbx][nby] = 1
                q.append((nrx,nry,nbx,nby,cnt+1))
    return 0


N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
visited = [[[[0]*M for _ in range(N)] for _ in range(M)] for _ in range(N)]

rx = ry = 0
bx = by = 0

for i in range(N):
    for j in range(M):
        if board[i][j] == 'R':
            rx, ry = i, j
            board[i][j] = '.'
        elif board[i][j] == 'B':
            bx, by = i, j
            board[i][j] = '.'

visited[rx][ry][bx][by] = 1
print(bfs(rx, ry, bx, by, 0))
