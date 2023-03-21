from collections import deque
import sys
input = sys.stdin.readline

dy = [-1,1,0,0]
dx = [0,0,-1,1]

def bfs(fire, sy, sx):
    f_q = deque(fire)
    while f_q:
        fy, fx, t = f_q.popleft()
        for i in range(4):
            nfy, nfx = fy+dy[i], fx+dx[i]
            if 0 <= nfy < h and 0 <= nfx < w and visited[nfy][nfx] == -1:
                if b_map[nfy][nfx] == '.':
                    visited[nfy][nfx] = t+1
                    f_q.append((nfy,nfx,t+1))

    s_q = deque([(sy, sx, 0)])
    while s_q:
        sy, sx, t = s_q.popleft()
        for i in range(4):
            nsy, nsx = sy+dy[i], sx+dx[i]
            if 0 <= nsy < h and 0 <= nsx < w:
                if b_map[nsy][nsx] == '.':
                    if visited[nsy][nsx] == -1 or visited[nsy][nsx] > t+1:
                        visited[nsy][nsx] = 0
                        s_q.append((nsy,nsx,t+1))
            else:
                return t+1
    else:
        return "IMPOSSIBLE"

T = int(input())
for _ in range(T):
    w, h = map(int, input().split())
    b_map = [list(input().rstrip()) for _ in range(h)]
    visited = [[-1]*w for _ in range(h)]
    sy = sx = 0
    fire = []
    for i in range(h):
        for j in range(w):
            if b_map[i][j] == '@':
                visited[i][j] = 0
                b_map[i][j] = '.'
                sy,sx = i,j
            if b_map[i][j] == '*':
                visited[i][j] = 0
                fire.append((i,j,0))
    print(bfs(fire,sy,sx))
