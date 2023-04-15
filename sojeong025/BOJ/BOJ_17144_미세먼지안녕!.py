import sys
input = sys.stdin.readline

# r*c 격자판 | t초
r, c, t = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(r)]

# 공기청정기 위치 찾기
# 공기청정기가 설치된 곳은 -1이고 위 아래 총 2칸 차지
for i in range(r):
    if arr[i][0] == -1:
        top = i
        bottom = i + 1
        break

# 초 단위로 미세먼지가 퍼지는 함수
def dust():
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    # 미세먼지 퍼진 값 저장
    dust_map = [[0] * c for _ in range(r)]
    for x in range(r):
        for y in range(c):
            if arr[x][y] == 0 or arr[x][y] == -1:
                continue
            dust = arr[x][y] // 5
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < r and 0 <= ny < c and arr[nx][ny] != -1:
                    dust_map[nx][ny] += dust
                    dust_map[x][y] -= dust
    for x in range(r):
        for y in range(c):
            arr[x][y] += dust_map[x][y]

# 공기청정기가 바람 위로 이동
def move_up():
    # 좌 상 우 하
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    x, y = top, 1
    direct = 0
    clean = 0
    while True:
        nx = x + dx[direct]
        ny = y + dy[direct]
        if x == top and y == 0:
            break
        if not 0 <= nx < r or not 0 <= ny < c:
            direct += 1
            continue
        arr[x][y], clean = clean, arr[x][y]
        x, y = nx, ny
        # print(1)

# 공기청정기 바람 아래로 이동
def move_down():
    # 좌 하 우 상
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    x, y = bottom, 1
    direct = 0
    clean = 0
    while True:
        nx = x + dx[direct]
        ny = y + dy[direct]
        if x == bottom and y==0:
            break
        if not 0 <= nx < r or not 0 <= ny < c:
            direct += 1
            continue
        arr[x][y], clean = clean, arr[x][y]
        x, y = nx, ny

# t초 동안 시뮬레이션
for _ in range(t):
    dust()
    move_up()
    move_down()

ans = 0
for i in range(r):
    for j in range(c):
        if arr[i][j] > 0:
            ans += arr[i][j]

print(ans)


