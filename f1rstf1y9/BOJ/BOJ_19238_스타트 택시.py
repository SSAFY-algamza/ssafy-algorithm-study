from collections import deque

N, M, fuel = map(int, input().split())
taxi_map = [list(map(int, input().split())) for _ in range(N)]
cur_x, cur_y = map(int, input().split())
cur_x, cur_y = cur_x - 1, cur_y - 1

start_map = [[0] * N for _ in range(N)]
end = {}
for i in range(1, M+1):
    sx, sy, ex, ey = map(int, input().split())
    start_map[sx-1][sy-1] = i
    e = end.get((ex-1, ey-1))
    if e:
        e.append(i)
    else:
        end[(ex-1, ey-1)] = [i]


delta = [(-1,0),(0,-1),(0,1),(1,0)]

def find_min_cost(x, y, fuel):
    min_x, min_y, min_f = -1, -1, 1e9
    q = deque([(x, y, 0)])
    while q:
        x, y, f = q.popleft()
        if start_map[x][y]:
            if f < min_f:
                min_x, min_y, min_f = x, y, f
            elif f == min_f:
                if x < min_x or (x==min_x and y < min_y):
                    min_x, min_y, min_f = x, y, f
        if fuel <= f:
            continue
        for dx, dy in delta:
            nx, ny = x+dx, y+dy
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if start_map[nx][ny]:
                    if f+1 < min_f:
                        min_x, min_y, min_f = nx, ny, f+1
                    elif f+1 == min_f:
                        if nx < min_x or (nx == min_x and ny < min_y):
                            min_x, min_y, min_f = nx, ny, f + 1
                if not taxi_map[nx][ny]:
                    visited[nx][ny] = 1
                    q.append((nx, ny, f+1))
    return min_x, min_y, min_f

def go_destination(x, y, fuel):
    q = deque([(x, y, 0)])
    while q:
        x, y, f = q.popleft()
        if customer in end.get((x, y), []):
            return x, y, f
        if fuel <= f:
            return -1, -1, -1
        for dx, dy in delta:
            nx, ny = x+dx, y+dy
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if customer in end.get((nx, ny), []):
                    return nx, ny, f+1
                if not taxi_map[nx][ny]:
                    visited[nx][ny] = 1
                    q.append((nx, ny, f+1))
    return -1, -1, -1

for _ in range(M):
    # 최단 거리 승객 찾기 -> 연료 깎고, 택시 해당 승객 위치로 이동
    visited = [[0] * N for _ in range(N)]
    visited[cur_x][cur_y] = 1
    cur_x, cur_y, f = find_min_cost(cur_x, cur_y, fuel)
    if cur_x == -1:
        print(-1)
        break
    fuel -= f
    customer = start_map[cur_x][cur_y]
    start_map[cur_x][cur_y] = 0

    # 태운 승객 목적지로 이동
    visited = [[0] * N for _ in range(N)]
    visited[cur_x][cur_y] = 1
    cur_x, cur_y, f = go_destination(cur_x, cur_y, fuel)
    if cur_x == -1:
        print(-1)
        break
    fuel += f
    end[(cur_x, cur_y)].remove(customer)
else:
    print(fuel)