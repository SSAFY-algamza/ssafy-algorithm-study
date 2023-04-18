import sys
input = sys.stdin.readline

R, C, T = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(R)]
vaccum = []
for r in range(R):
    if A[r][0] == -1:
        vaccum = [(r, 0), (r+1,0)]
        break

delta = [(1,0),(-1,0),(0,1),(0,-1)]
def spread_dust():
    result = [[0] * C for _ in range(R)]
    for r in range(R):
        for c in range(C):
            if not A[r][c] or A[r][c] == -1:
                continue
            dust = A[r][c]//5
            for dr, dc in delta:
                nr, nc = r+dr, c+dc
                if 0 <= nr < R and 0 <= nc < C and A[nr][nc] != -1:
                    result[nr][nc] += dust
                    result[r][c] -= dust
    for r in range(R):
        for c in range(C):
            A[r][c] += result[r][c]

up_delta = [(0,1),(-1,0),(0,-1),(1,0)]
down_delta = [(0,1),(1,0),(0,-1),(-1,0)]
def spread_wind(cx, cy, d):
    if d == 0:
        dt = up_delta
    else:
        dt = down_delta
    i = 0
    prev = 0
    while True:
        nx, ny = cx+dt[i][0], cy+dt[i][1]
        if (cx, cy) == vaccum[d]:
            break
        if not 0 <= nx < R or not 0 <= ny < C:
            i += 1
            continue
        A[cx][cy], prev = prev, A[cx][cy]
        cx, cy = nx, ny

while T:
    spread_dust()
    spread_wind(vaccum[0][0], 1, 0)
    spread_wind(vaccum[1][0], 1, 1)
    T -= 1

ans = 0
for i in range(R):
    for j in range(C):
        ans += A[i][j] if A[i][j] != -1 else 0
print(ans)
