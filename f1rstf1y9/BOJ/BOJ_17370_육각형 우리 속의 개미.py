delta = [[(-1,-1),(-1,1),(1,0)], [(1,-1),(1,1),(-1,0)]]

def bt(x, y, case, bx, by, cnt):
    global ans
    if cnt >= N:
        return
    d = delta[case]
    case = 0 if case else 1
    for i in range(3):
        nx, ny = x+d[i][0], y+d[i][1]
        if (nx,ny) == (bx,by): # 직전에 방문했던 곳
            continue
        if visited[nx][ny] and cnt+1 == N: # 회전횟수 만족하면서 방문했던 곳 지남
            ans += 1
            continue
        if visited[nx][ny]: # 회전 횟수 채우기 전에 이미 방문했던 곳 지남
            continue
        visited[nx][ny] = 1
        bt(nx, ny, case, x, y, cnt+1)
        visited[nx][ny] = 0

N = int(input())
visited = [[0]*50 for _ in range(50)]
visited[25][25] = visited[26][24] = 1
ans = 0
bt(26, 24, 0, 25, 25, 0) # 현재 위치, delta종류, 회전 횟수, 왔던길 체크용, 카운트
print(ans)