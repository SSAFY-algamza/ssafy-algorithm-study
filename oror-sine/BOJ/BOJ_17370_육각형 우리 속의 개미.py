N = int(input())

ds = ((-1, 0), (-1, 1), (1, 1), (1, 0), (1, -1), (-1, -1))
def get_ds(current):
    return (current+1)%6, (current-1)%6

ans = 0
visited = [[False]*(2*N+1)for _ in range((2*N+1))]
visited[N][N] = True
visited[N-1][N] = True

def backtrack(depth, coord, prev_d):
    global ans
    if depth > N:
        return
    ncoord = (coord[0]+ds[prev_d][0], coord[1]+ds[prev_d][1])
    if not visited[ncoord[0]][ncoord[1]] :
        visited[ncoord[0]][ncoord[1]] = True
        for nd in get_ds(prev_d):
            backtrack(depth+1, ncoord, nd)
        visited[ncoord[0]][ncoord[1]] = False
    elif depth == N:
        ans += 1
        
backtrack(0, (N-1, N), 0)
print(ans)