def dfs(x,y,hp,milk):  # dfs 함수
    global ans

    for mx,my in mint_choco:
        if village[mx][my] == 2:  # 현재까지 마시지 않은 우유인가
            dist = abs(x-mx)+abs(y-my)  # 거리 차이
            if dist <= hp:  # 거리가 현재 체력으로 갈 수 있는가
                village[mx][my] = 0  # 해당 위치 우유 마시고
                dfs(mx,my,hp-dist+H,milk+1)
                village[mx][my] = 2  # 복구 시켜준다.

    if abs(hx-x)+abs(hy-y) <= hp:
        ans = max(ans,milk)

N,M,H = map(int,input().split())
village = []
for _ in range(N):
    village.append(list(map(int,input().split())))

ans = 0
mint_choco = []
hx, hy = 0, 0
for i in range(N):
    for j in range(N):
        if village[i][j] == 2:
            mint_choco.append([i, j])  # 민트초코가 있는 위치좌표 담기
        elif village[i][j] == 1:
            hx, hy = i, j  # 집이 있는 곳. 시작 위치

dfs(hx,hy,M,0)
print(ans)