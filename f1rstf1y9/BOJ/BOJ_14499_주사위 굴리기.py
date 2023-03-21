def move_dice(d):
    if d == 1:
        dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1]
    elif d == 2:
        dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]
    elif d == 3:
        dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]
    elif d == 4:
        dice[0], dice[2], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[2]

move_d = [0, (0,1),(0,-1),(-1,0),(1,0)]
N, M, x, y, K = map(int, input().split())
m_map = [list(map(int, input().split())) for _ in range(N)]
orders = list(map(int, input().split()))
dice = [0]*6
for d in orders:
    dx, dy = move_d[d]
    nx, ny = x+dx, y+dy
    if 0 <= nx < N and 0 <= ny < M:
        x, y = nx, ny
        move_dice(d)
        if m_map[x][y] == 0:
            m_map[x][y] = dice[5]
        else:
            dice[5] = m_map[x][y]
            m_map[x][y] = 0
        print(dice[0])
