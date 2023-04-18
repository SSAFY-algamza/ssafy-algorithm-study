from collections import deque
'''
처음에 덱을 사용 안하고 풀었는데, 시간 초과가 떴다.
찾아봤더니, pop(0)이 시간복잡도가 O(n)이고 popleft()가 O(1)이라고 한다.
'''

N,M = map(int,input().split())
tomatoes = [list(map(int,input().split()))for _ in range(M)]
delta = [(1,0),(-1,0),(0,1),(0,-1)]
Q = deque()
ans = 0

check_0 = 0
for i in range(M):
    for j in range(N):
        if tomatoes[i][j] == 1:
            Q.append((i,j))
        elif tomatoes[i][j] == 0:
            check_0 += 1

if check_0 == 0:
    print(0)
    exit(0)

while Q:  # 나한테 익숙한 while 문 반복으로 bfs를 만듦.
    p = Q.popleft()

    for k in range(4):
        ni = p[0] + delta[k][0]
        nj = p[1] + delta[k][1]
        if 0 <= ni < M and 0 <= nj < N and tomatoes[ni][nj] == 0 :
            tomatoes[ni][nj] = tomatoes[p[0]][p[1]] + 1  # 방문 기록
            Q.append((ni, nj))

for i in range(M):
    for j in range(N):
        if tomatoes[i][j] == 0:
            print(-1)
            exit(0)
    ans = max(ans,max(tomatoes[i]))

print(ans-1)