import sys
from collections import deque
N = int(sys.stdin.readline())
scale = 2
exp = 0
ds = ((-1, 0), (0, -1), (1, 0), (0, 1))
fish = [0]*6
grid = [[0]*N for _ in range(N)]
pos = None
for r in range(N):
    for c, cell in enumerate(sys.stdin.readline().split()):
        if cell != "0":
            if cell == "9":
                pos = (r, c)
                continue
            grid[r][c] = int(cell)
            fish[int(cell)-1] += 1


def is_any_food():
    for fish_scale in range(1, min(scale, 7)):
        if fish[fish_scale-1]:
            return True
    return False


def find_food(coord):
    global grid
    global t
    global scale
    global exp
    Q = deque([coord])
    visited = [[False]*N for _ in range(N)]
    visited[coord[0]][coord[1]] = True
    food = []
    tmp = 0
    while Q and not food:
        tmp += 1
        for _ in range(len(Q)):
            r, c = Q.popleft()
            for dr, dc in ds:
                if 0 <= (nr := r+dr) < N and 0 <= (nc := c+dc) < N:
                    if visited[nr][nc] or grid[nr][nc] > scale:
                        continue
                    visited[nr][nc] = True
                    if 0 < grid[nr][nc] < scale:
                        food.append((nr, nc))
                        continue
                    Q.append((nr, nc))
    if food:
        t += tmp
        coord = min(food)
        fish[grid[coord[0]][coord[1]]-1] -= 1
        grid[coord[0]][coord[1]] = 0
        if (exp := exp+1) == scale:
            scale += 1
            exp = 0
        if is_any_food():
            find_food(coord)
    else:
        return


t = 0
if is_any_food():
    find_food(pos)
print(t)
