from copy import deepcopy
import sys
input = sys.stdin.readline

fish_delta = [(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1)] # ←, ↖, ↑, ↗, →, ↘, ↓, ↙
shark_delta = [0,(-1,0),(0,-1),(1,0),(0,1)] # 상 좌 하 우

# 초기화 & 입력받기
fish = [[[] for _ in range(4)] for _ in range(4)]
smell = [[0]*4 for _ in range(4)]
M, S = map(int, input().split())
for _ in range(M):
    x, y, d = map(int, input().split())
    fish[x-1][y-1].append(d-1)

sx, sy = map(int, input().split())
sx, sy = sx-1, sy-1


# 2. 모든 물고기가 한 칸 이동 => 상어칸, 냄새칸, 범위밖 이동X
def is_valid_move(x, y):
    if not (0 <= x < 4 and 0 <= y < 4):
        return False
    if x == sx and y == sy:
        return False
    if smell[x][y]:
        return False
    return True

def move_fish():
    new_fish = [[[] for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            for f in fish[i][j]:
                for d in range(8):
                    direction = (f-d)%8
                    dx, dy = fish_delta[direction]
                    nx, ny = i+dx, j+dy
                    if is_valid_move(nx, ny):
                        new_fish[nx][ny].append(direction)
                        break
                else:
                    new_fish[i][j].append(f)
    return new_fish

# 3. 상어 연속 3칸 이동
def compare_way(a, b):
    if a < b:
        return a
    return b

def find_best_way(x, y, way, kill, n): # 현재 위치, 현재 이동방향, 현재 제외시킨 물고기 수, 현재 이동 수
    global best_way, best_kill
    if n == 3:
        if kill > best_kill:
            best_way, best_kill = way, kill
        elif kill == best_kill:
            best_way = compare_way(best_way, way)
        return
    for d in range(1, 5):
        dx, dy = shark_delta[d]
        nx, ny = x+dx, y+dy
        if 0 <= nx < 4 and 0 <= ny < 4:
            if visited[nx][ny]:
                find_best_way(nx, ny, way+str(d), kill, n+1)
            else:
                visited[nx][ny] = 1
                find_best_way(nx, ny, way+str(d), kill+len(fish[nx][ny]), n+1)
                visited[nx][ny] = 0

def move_shark(sx, sy, way):
    for w in way:
        dx, dy = shark_delta[int(w)]
        sx, sy = sx+dx, sy+dy
        if fish[sx][sy]:
            fish[sx][sy] = []
            smell[sx][sy] = 3
    return sx, sy

# 4. 2번 전 연습에서 생긴 물고기 냄새 격자에서 지우기
def remove_smell():
    for i in range(4):
        for j in range(4):
            if smell[i][j]:
                smell[i][j] -= 1


# 5. 복제마법 완료
def apply_copy():
    for i in range(4):
        for j in range(4):
            fish[i][j].extend(copy_fish[i][j])



# 마법 연습 시작
for _ in range(S):
    copy_fish = deepcopy(fish)
    fish = move_fish()
    best_way = '999'
    best_kill = 0
    visited = [[0]*4 for _ in range(4)]
    find_best_way(sx, sy, '', 0, 0)
    sx, sy = move_shark(sx, sy, best_way)
    remove_smell()
    apply_copy()


ans = 0
for i in range(4):
    for j in range(4):
       ans += len(fish[i][j])
print(ans)