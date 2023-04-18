from collections import deque

N,M = map(int,input().split())
maze = [list(map(int,input())) for _ in range(N)]

S = (0,0)
E = (N-1,M-1)
visited = [[0]*M for _ in range(N)]  # 방문 기록할 곳
delta = [(1,0), (-1,0), (0,1), (0,-1)]  # 델타 이동 좌표
ans = 0  # 정답 초기화

visited[S[0]][S[1]] = 1 # 방문 표시
Q = deque([S])  # 큐에 담기

flag = True
while Q:  # 큐 있는 동안 계속 탐색

    now = Q.popleft()

    for k in range(4):
        ni = now[0] + delta[k][0]
        nj = now[1] + delta[k][1]  # 다음 좌표 생성
        if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0:  # 인덱스를 벗어나지 않고, 방문 안한 곳이면
            if (ni,nj) == E:  # 그 곳이 마지막 좌표이면
                maze[ni][nj] = maze[now[0]][now[1]] + 1 # 거리 기록해주고
                ans = maze[ni][nj]  # 그 값을 답에 할당한다
            elif maze[ni][nj] == 1:  # 그 곳이 이동할 수 있는 곳이면
                maze[ni][nj] = maze[now[0]][now[1]] + 1  # 거리 기록해주고
                visited[ni][nj] = 1  # 방문 표시도 해주고
                Q.append((ni,nj))  # 다음에 갈 곳이니까 큐에 담는다
        if ans:  # 답에 값이 생겼으면 반복문을 완전히 탈출 해야 한다
            flag = False
            break
    if flag == False:
        break

print(ans)