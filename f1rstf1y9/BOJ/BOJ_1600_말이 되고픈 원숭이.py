from collections import deque
delta = [(-1,0),(1,0),(0,-1),(0,1),(-2,-1),(-1,-2),(-1,2),(-2,1),(1,-2),(2,-1),(1,2),(2,1)]

def bfs(x,y,k,cnt): #현재 위치, 남은 말 이동횟수, 전체 이동횟수
    ans = 1e9
    q = deque([(x,y,k,cnt)])
    while q:
        x, y, k, cnt = q.popleft()
        # 현재 카운트가 이미 구한 ans값보다 커지면 pass
        if cnt >= ans:
            continue
        # 도착했으면 ans 갱신 후 pass
        if (x,y) == (H-1, W-1):
            ans = min(ans, cnt)
            continue

        # 말 횟수가 남아 있으면
        if k > 0:
            limit = 12
        else: # 안남아있으면
            limit = 4
        for i in range(limit):
            nx, ny = x+delta[i][0], y+delta[i][1]
            if 0 <= nx < H and 0 <= ny < W:
                if board[nx][ny]: # 장애물 있으면
                    continue
                # 말 움직임
                if i >= 4:
                    if not visited[nx][ny][k-1]:
                        visited[x][y][k] = 1
                        q.append((nx, ny, k-1, cnt+1))
                else:
                    if not visited[nx][ny][k]:
                        visited[x][y][k] = 1
                        q.append((nx, ny, k, cnt+1))
    return ans
K = int(input())
W, H = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(H)]
visited = [[[0]*(K+1) for _ in range(W)] for _ in range(H)]
visited[0][0][K] = 1
ans = bfs(0,0,K,0)
print(ans if ans != 1e9 else -1)

'''
3
4 5
0 1 1 1
1 1 0 1
1 1 1 1
1 1 1 0
1 1 1 0

---
1
4 4
0 0 0 0
0 0 0 0
0 0 1 1
0 0 1 0

---
1
5 5
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 1 1
0 0 0 1 0
'''