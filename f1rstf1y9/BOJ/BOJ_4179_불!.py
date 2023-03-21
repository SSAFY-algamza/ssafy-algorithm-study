from collections import deque
import sys

input = sys.stdin.readline

dy = [-1,1,0,0]
dx = [0,0,-1,1]

def bfs(f_q, jh_y, jh_x):
    while f_q:
        fy, fx, t = f_q.popleft()
        for i in range(4):
            nfy,nfx = fy+dy[i], fx+dx[i]
            if 0 <= nfy < R and 0 <= nfx < C and visited[nfy][nfx] == -1:
                if maze[nfy][nfx] != '#':
                    visited[nfy][nfx] = t+1
                    f_q.append((nfy, nfx, t+1))

    jh_q = deque([(jh_y, jh_x, 0)])

    while jh_q:
        jh_y, jh_x, t = jh_q.popleft()
        for i in range(4):
            jh_ny, jh_nx = jh_y+dy[i], jh_x+dx[i]
            if 0 <= jh_ny < R and 0 <= jh_nx < C:
                if maze[jh_ny][jh_nx] == '.':
                    # 불이 퍼진 시점보다 정훈이가 빨리 도착
                    if visited[jh_ny][jh_nx] == -1 or visited[jh_ny][jh_nx] > t+1:
                        jh_q.append((jh_ny, jh_nx, t+1))
                        visited[jh_ny][jh_nx] = 0
            else:
                return t+1

    return 'IMPOSSIBLE'


R, C = map(int, input().rstrip().split())
maze = [list(input().rstrip()) for _ in range(R)]
visited = [[-1]*C for _ in range(R)]

jh_y, jh_x = 0, 0
fire = deque([])

for i in range(R):
    for j in range(C):
        if maze[i][j] == 'J':
            jh_y, jh_x = i, j
        if maze[i][j] == 'F':
            fire.append((i,j,0))
print(bfs(fire, jh_y, jh_x))



'''
INPUT1:

3 4
####
#FJ.
####

ANSWER1:

2

INPUT2:

6 7
###.###
#F#.#F#
#.....#
#.....#
#..J..#
#######

ANSWER2:

5
'''