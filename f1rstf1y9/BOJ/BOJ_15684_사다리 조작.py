def is_valid():
    cur = [i for i in range(N)]
    for i in range(H):
        for j in range(N-1):
            if ladder[i][j]:
                cur[j], cur[j+1] = cur[j+1], cur[j]
    return cur == res
def bt(cnt, idx):
    global ans
    if cnt > 3 or cnt > ans:
        return

    if is_valid():
        ans = min(ans, cnt)
        return

    for i in range(idx, H):
        for j in range(N-1):
            if not ladder[i][j]:
                if (j-1 >= 0 and ladder[i][j-1]) or (j+1 < N-1 and ladder[i][j+1]):
                    continue
                ladder[i][j] = 1
                bt(cnt+1, i)
                ladder[i][j] = 0

N, M, H = map(int, input().split())
ladder = [[0]*(N-1) for _ in range(H)]
cur = [i for i in range(N)]
res = [i for i in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    ladder[a-1][b-1] = 1

for i in range(H):
    for j in range(N-1):
        if ladder[i][j]:
            cur[j], cur[j+1] = cur[j+1], cur[j]
ans = 4
bt(0, 0)
print(ans if ans != 4 else -1)