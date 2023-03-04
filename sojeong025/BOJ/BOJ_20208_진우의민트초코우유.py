'''
구현 아이디어
map의 민트 우유 위치 리스트에 mint[]에 저장
네 방향을 다 조사하지 않고 민초 있는 곳으로 한 번에 이동
민초1 -> 민초2
조사해야 할 것 : map[i][j]가 2인가 / 현재 체력으로 가는가
위 조사를 통과하면, 우유 마시고
'''

import sys
sys.stdin = open('input.txt')

# N 민초마을의 크기 M 초기체력 H 민초 마시고 증가하는 체력
N, M, H = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(N)]

def DFS(hx, hy , hp, drink):
    global answer

    for x, y in mint:
        # 민초 안마셨으면 진행
        if map[x][y] == 2:
            dis = abs(hx - x) + abs(hy - y)
            # 현재 체력으로 갈 수 있는 거리인지 체크
            if dis <= hp:
                map[x][y] = 0
                # 재귀를 도는데, 체력은 현재 체력에 + H - 거리, 우유 마신거 count
                DFS(x, y, hp + H - dis, drink + 1)
                map[x][y] = 2

    if abs(hx - home_x) + abs(hy - home_y) <= hp:
        answer = max(answer, drink)


home_x, home_y = 0, 0
mint = []
answer = 0
for i in range(N):
    for j in range(N):
        if map[i][j] == 1:
            home_x, home_y = i, j
        if map[i][j] == 2:
            mint.append((i, j))

DFS(home_x, home_y, M, 0)
print(answer)
