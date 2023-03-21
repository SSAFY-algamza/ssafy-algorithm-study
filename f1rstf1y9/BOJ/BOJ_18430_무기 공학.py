delta = [((1,0),(0,-1)), ((-1,0),(0,-1)), ((-1,0),(0,1)), ((0,1),(1,0))]
ans = 0
def bt(y,x,cur):
    global ans

    if x == M:
        y, x = y+1, 0

    if y == N:
        ans = max(cur, ans)
        return
    if not visited[y][x]:
        for i in range(4):
            d = delta[i]
            ny1, nx1, ny2, nx2 = y+d[0][0], x+d[0][1], y+d[1][0], x+d[1][1]
            if 0 <= ny1 < N and 0 <= nx1 < M and 0 <= ny2 < N and 0 <= nx2 < M:
                if not visited[ny1][nx1] and not visited[ny2][nx2]:
                    visited[y][x] = visited[ny1][nx1] = visited[ny2][nx2] = 1
                    bt(y, x+1, cur+woods[y][x]*2+woods[ny1][nx1]+woods[ny2][nx2])
                    visited[y][x] = visited[ny1][nx1] = visited[ny2][nx2] = 0
    bt(y, x+1, cur)

N, M = map(int, input().split())
woods = [list(map(int, input().split())) for _ in range(N)]

visited = [[0]*M for _ in range(N)]
bt(0,0,0)
print(ans)
