import sys
sys.stdin = open('input.txt')

# 모든 섬을 다리로 연결 한다. (MST? X)
# 각 칸은 땅(1) 이거나 바다(0)
# 가로로 놓아진 다리는 섬과 가로로 연결되어야 한다, 세로도 마찬가지
# 가로의 다리가 1이거나 가로의 방향이 중간에 바뀌어선 안된다
# 다리가 교차하는 경우는 O, 다리의 길이를 계산할 때, 각 칸이 각 다리의 길이에 모두 포함
# 다리 길이의 최솟값을 구하시옹

# 1. 이미 연결된 섬은 또 연결하지 않는다. (MST..?)
# 2. 연결되지 않은 섬은 가장 가까운 섬과 (하지만 길이 > 1) 연결한다
# 3. 다리를 만들때는 일직선으로 만드는 것 자체는 while문 + 델타탐색으로 해야할 듯
# 4. 아마 다리가 교차하는 경우는 섬이 연결된게 아닐테니까, 맵 자체로 섬의 연결 여부 판단 X

# 1. 먼저 각 섬의 정보를 저장. BFS
# 2. while + delta 로 다리가 만들어지면, 다리의 길이, 연결되는 섬의 정보를 저장
# 3. kruskal 알고리즘을 활용해 섬이 모두 연결되면서 다리의 길이가 가장 짧은 값 저장

from collections import deque

di = [0, 0, -1, 1]
dj = [-1, 1, 0, 0]

# 대표 원소 정리
def find_set(x):
    while x != parent[x]:
        x = parent[x]
    return x

# 집합 생성
def union(x, y):
    parent[find_set(y)] = find_set(x)

# 값을 각 섬의 id로 변경
def BFS(start):
    global islands_id
    q = deque()
    q.append(start)
    while q:
        i, j = q.popleft()
        chart[i][j] = islands_id
        visited[i][j] = 1
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < M:
                if chart[ni][nj] and not visited[ni][nj]:
                    visited[ni][nj] = 1
                    q.append((ni, nj))
                    chart[ni][nj] = islands_id

    islands_id += 1
    return

# 다리 길이 저장
def build_bridge(r, c, d):
    global bridges
    rlt = 0
    i, j = r, c
    id = chart[r][c]

    if d == 1:
        k = 2
    elif d == 2:
        k = 3
    elif d == 3:
        k = 0
    elif d == 4:
        k = 1
    while True:
        ni = i + di[k]
        nj = j + dj[k]
        i, j = ni, nj
        if 0 <= ni < N and 0 <= nj < M:
            if not chart[ni][nj]:
                rlt += 1
                continue
            elif chart[ni][nj] == chart[r][c]:
                return
            elif chart[ni][nj] and chart[ni][nj] != id:
                if bridges[chart[r][c]][chart[ni][nj]] >= rlt > 1:
                    bridges[chart[r][c]][chart[ni][nj]] = rlt
                    return
                else:
                    return
        else:
            return

N, M = map(int, input().split())
chart = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

# 각 섬의 idx에 섬의 id를 부여해 구분
islands_id = 1
for i in range(N):
    for j in range(M):
        if chart[i][j] and not visited[i][j]:
            BFS((i, j))


# id가 다른 섬들끼리 최단 직선거리를 측정해, 해당 섬 사이의 거리로 갱신, direction == 1, 2, 3, 4 (상 하 좌 우 방향)
bridges = [[N*M] * islands_id for _ in range(islands_id)]
for i in range(N):
    for j in range(M):
        if chart[i][j]:
            build_bridge(i, j, 1)
            build_bridge(i, j, 2)
            build_bridge(i, j, 3)
            build_bridge(i, j, 4)

edge = []
for i in range(islands_id):
    for j in range(i+1, islands_id):
        if 1 < bridges[i][j] < N*M:
            edge.append([i, j, bridges[i][j]])

# Kruskal 알고리즘
# 가중치 기준 정렬
edge.sort(key=lambda x : x[2])
# 대표 원소 정보
parent = list(range(islands_id))
result = 0
cnt = 1
for s, e, w in edge:
    # 사이클을 형성하지 않도록 대표원소 정보가 다를떄만
    if find_set(s) != find_set(e):
        union(s, e)     # 집합 형성
        result += w     # 가중치 합
        cnt += 1

if islands_id-1 == cnt:
    print(result)
else:
    print(-1)