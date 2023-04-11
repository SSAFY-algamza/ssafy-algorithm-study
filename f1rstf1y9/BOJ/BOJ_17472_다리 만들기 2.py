'''
1. 각 섬을 같은 번호로 묶기
2. 같은 번호로 묶인 각 섬에서 다른 번호의 섬까지 길이 1 이상으로 연결할 수 있는 경우 간선 정보 추가
3. 크루스칼 알고리즘 사용하여 최소 스패닝 트리 구하면서,
   union할 때마다 다리 길이 ans 변수에 더해주기
4. 각 섬의 최종 부모들이 같지 않다면, 최소 스패닝 트리를 구하지 못한 것이므로 -1 출력,
   아니면 ans에 저장된 다리 길이 최솟값 출력

'''

import sys
from collections import deque
input = sys.stdin.readline

### (0) 입력 ###

# N : 지도의 세로 크기, M : 지도의 가로 크기
N, M = map(int, input().split())
# 지도 정보 입력 받기
map_info = [list(map(int, input().split())) for _ in range(N)]

# BFS 탐색을 위한 방문 체크 리스트 & 델타 이동 리스트
visited = [[0]*M for _ in range(N)]
delta = [(1,0),(-1,0),(0,1),(0,-1)]



### (1) BFS 탐색을 통해 같은 섬인 칸에 번호 붙이기 ###

# 각 번호의 섬을 구성하는 땅의 좌표를 저장할 리스트
lands = [[] for _ in range(2)]
def bfs(x, y, n):
    land = []
    q = deque([(x, y)])
    while q:
        x, y = q.popleft()
        visited[x][y] = 1
        map_info[x][y] = n
        land.append((x, y))
        for dx, dy in delta:
            nx, ny = x+dx, y+dy
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                if map_info[nx][ny] == 1:
                    q.append((nx, ny))
    return land

num = 2 # 0은 바다, 1은 땅으로 정해져 있으므로 2번부터
for i in range(N):
    for j in range(M):
        if map_info[i][j] == 1:
            lands.append(bfs(i, j, num))
            num += 1



### (2) 섬과 섬 사이의 간선 구하기 ###

# 간선 정보를 담을 리스트
edges = []
def get_edge(n, x, y, dx, dy):
    cost = 0
    nx, ny = x+dx, y+dy
    while 0 <= nx < N and 0 <= ny < M:
        # 바다면 계속해서 탐색
        if map_info[nx][ny] == 0:
            nx, ny = nx + dx, ny + dy
            cost += 1
        # 자기 섬이 아닌 땅 만나면 탐색 중지하고, 다리 길이에 따라 간선 정보 추가
        elif map_info[nx][ny] != n:
            # 연결한 다리 길이가 1보다 크면, (출발지, 도착지, 다리길이)를 edges에 추가
            if cost > 1:
                edges.append((n, map_info[nx][ny], cost))
            return
        # 자기 섬인 땅 만나면 탐색 중지
        else:
            return

# 섬번호가 2번부터 붙으므로 2번 섬부터 마지막 섬까지 탐색해서 간선 구하기
for i in range(2, num):
    for x, y in lands[i]:
        for dx, dy in delta:
            get_edge(i, x, y, dx, dy)



### (3) 크루스칼 알고리즘 사용하여 최소 스패닝 트리 구하기 ###
def get_parent(n):
    if parent[n] != n:
        parent[n] = get_parent(parent[n])
    return parent[n]

def union(a, b):
    a, b = get_parent(a), get_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 간선정보를 다리 길이가 짧은 순으로 정렬
edges.sort(key=lambda x:x[2])

# 각 노드(섬)의 부모를 자기자신으로 초기화
parent = [i for i in range(num)]

ans = 0
for edge in edges:
    a, b, cost = edge
    if get_parent(a) != get_parent(b):
        union(a, b)
        ans += cost


### (4) 각 섬의 최종 부모 확인하여 경우에 따라 정답 출력 ###
p = get_parent(2)
for i in range(3, num):
    if get_parent(i) != p:
        print(-1)
        break
else:
    print(ans)