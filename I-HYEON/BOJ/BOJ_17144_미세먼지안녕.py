import sys
input = sys.stdin.readline

R, C, T = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(R)]

def move(x,y):
    result = grid[x][y]
    for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        ni = x + di
        nj = y + dj

        if 0 <= ni < R and 0 <= nj < C and grid[ni][nj] != -1 :
            result += grid[ni][nj]//5
            result -= grid[x][y]//5

    return result

time = 0
while time != T:
    temp_grid = [[0] * C for _ in range(R)]

    airs = []
    for r in range(R):
        for c in range(C):
            if grid[r][c] != -1:  # 공기청정기가 아는 곳은 다 돌면서
                temp_grid[r][c] = move(r, c)  # 이동 후 값을 구해서 temp_grid 같은 위치에 저장한다
            else:
                temp_grid[r][c] = -1
                airs.append((r, c))

    air1 = airs[0]
    air2 = airs[1]
    # air1 작동
    temp = 0
    for i in range(1, C):
        temp, temp_grid[air1[0]][i] = temp_grid[air1[0]][i], temp
    for i in range(air1[0]-1, -1, -1):
        temp, temp_grid[i][C-1] = temp_grid[i][C-1], temp
    for i in range(C-2, -1, -1):
        temp, temp_grid[0][i] = temp_grid[0][i], temp
    for i in range(1,air1[0]):
        temp, temp_grid[i][0] = temp_grid[i][0], temp

    # air2 작동

    temp = 0
    for i in range(1, C):
        temp, temp_grid[air2[0]][i] = temp_grid[air2[0]][i], temp
    for i in range(air2[0] + 1, R):
        temp, temp_grid[i][C - 1] = temp_grid[i][C - 1], temp
    for i in range(C - 2, -1, -1):
        temp, temp_grid[R-1][i] = temp_grid[R-1][i], temp
    for i in range(R-2, air2[0], -1):
        temp, temp_grid[i][0] = temp_grid[i][0], temp

    grid = temp_grid

    time += 1

ans = 0
for i in range(R):
    for j in range(C):
        if grid[i][j] != -1:
            ans += grid[i][j]

print(ans)