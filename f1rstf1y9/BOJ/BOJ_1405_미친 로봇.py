d_dict = {'E':(0,1), 'W':(0,-1), 'S':(1,0), 'N':(-1,0)}

def find_way(p, y, x, cnt):
    global ans

    if cnt == N:
        ans += p
        return
    for d in d_dict:
        dy, dx = d_dict[d]
        ny, nx = y+dy, x+dx
        if not visited[ny][nx] and 0 <= ny < 2*N+1 and 0 <= nx < 2*N+1:
            visited[ny][nx] = 1
            find_way(p*pos[d]*0.01, ny, nx, cnt+1)
            visited[ny][nx] = 0

N, e, w, s, n = map(int, input().split())
pos = {'E':e, 'W':w, 'S':s, 'N':n}

visited = [[0]*(2*N+1) for _ in range(2*N+1)]
visited[N][N] = 1

ans = 0
res = find_way(1, N, N, 0)
print(ans)
