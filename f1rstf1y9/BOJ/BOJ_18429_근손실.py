def bt(now, day):
    global ans
    if now < 500:
        return
    if day == N:
        ans += 1
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            bt(now-K+A[i], day+1)
            visited[i] = 0

N, K = map(int, input().split())
A = list(map(int, input().split()))
visited = [0]*N
ans = 0
bt(500, 0)
print(ans)
