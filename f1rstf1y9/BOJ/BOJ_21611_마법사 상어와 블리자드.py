'''
(N//2, N//2-1), (N//2-1, N//2-2) ..
(N//2+1, N//2-1), (N//2+2, N//2-2) ..
(N//2+1, N//2+1), (N//2+2, N//2+2) ..
(N//2-1, N//2+1), (N//2-2, N//2+2) ..
'''


N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
grid_num = [0]*(N*N)
delta = [(0,-1),(1,0),(0,1),(-1,0)]
ans_lst = [0]*4


# 달팽이 모양 좌표 구하기
n = N//2
x, y = n, n
num = 0
cnt = 1
while num < N*N:
    for dx, dy in delta:
        while num < N*N:
            x, y = x + dx, y + dy
            num += 1
            if num >= N*N:
                break
            grid_num[num] = (x,y)
            if (x, y) in [(n-cnt+1, n-cnt), (n+cnt, n-cnt), (n+cnt, n+cnt), (n-cnt, n+cnt)]:
                break
    cnt += 1

def move_balls():
    ball_list = []
    for i in range(1, N*N-1):
        x, y = grid_num[i]
        if grid[x][y]:
            ball_list.append(grid[x][y])
    for i in range(N*N-1):
        x, y = grid_num[i + 1]
        if i < len(ball_list):
            grid[x][y] = ball_list[i]
        else:
            grid[x][y] = 0

def check_boom():
    is_boom = False
    lst = [(grid_num[1][0], grid_num[1][1])]
    ball_num = grid[grid_num[1][0]][grid_num[1][1]]
    for i in range(2, N*N):
        x, y = grid_num[i]
        if grid[x][y] != ball_num:
            if len(lst) >= 4:
                is_boom = True
                for r, c in lst:
                    ans_lst[grid[r][c]] += 1
                    grid[r][c] = 0
            lst = [(x,y)]
            ball_num = grid[x][y]
        else:
            lst.append((x,y))
    return is_boom

def change_balls():
    new_grid = [[0]*N for _ in range(N)]
    ball_num = grid[grid_num[1][0]][grid_num[1][1]]
    ball_cnt = 1
    grid_idx = 0
    for i in range(2, N*N):
        x, y = grid_num[i]
        if ball_num != grid[x][y]:
            grid_idx += 1
            if grid_idx < N*N:
                nx, ny = grid_num[grid_idx]
                new_grid[nx][ny] = ball_cnt
            else:
                break
            grid_idx += 1
            if grid_idx < N*N:
                nx, ny = grid_num[grid_idx]
                new_grid[nx][ny] = ball_num
            else:
                break
            ball_cnt = 1
            ball_num = grid[x][y]
        else:
            ball_cnt += 1
    return new_grid


# M번 동안 블리자드 마법 시전
magic_d = [0,(-1,0),(1,0),(0,-1),(0,1)]
for _ in range(M):
    x, y = n, n
    d, s = map(int, input().split())
    dx, dy = magic_d[d]
    # 마법 시전
    for _ in range(s):
        x, y = x+dx, y+dy
        grid[x][y] = 0

    # 구슬 이동 -> 폭발 체크 -> (폭발 했으면) 구슬 이동 -> 폭발 체크 -> ...
    move_balls()
    while check_boom():
        move_balls()

    # 더 이상 폭발 진행x -> 구슬 변화
    grid = change_balls()

ans = 0
for i in range(4):
    ans += i*ans_lst[i]

print(ans)