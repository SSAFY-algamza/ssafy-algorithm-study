from collections import deque

N,M = map(int,input().split())  # 배열 세로, 가로 길이
ocean = [list(map(int,input().split())) for _ in range(N)]  # 아기 상어들이 있는 공간
delta = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

def bfs(x,y):  # bfs탐색하다가 1만나면 안전거리를 반환하는 함수.
    result = 0
    visited = [[0]*M for _ in range(N)]  # 방문 표시할 배열
    '''
    큐를 만들어서 현재좌표를 집어넣는다.
    와일문 반복을 돈다.
    큐에서 하나 뽑아서 8방향 델타로 다음 탐색할 좌표를 추가한다.
    1이라면 바로 중단한다.
    '''
    visited[x][y] = 1  # 방문 표시
    Q = deque([(x,y)])
    while Q:

        now = Q.popleft()
        for d in range(8):
            ni = now[0] + delta[d][0]
            nj = now[1] + delta[d][1]
            if 0<=ni<N and 0<=nj<M and visited[ni][nj] == 0:  # 범위 안이고 방문 안한 곳이면
                if ocean[ni][nj] == 1:  # 거기 아기상어가 있으면
                    visited[ni][nj] = visited[now[0]][now[1]] + 1  # 방문 기록
                    result = visited[ni][nj] - 1  # 시작할 때 시작하는 칸부터 1이었으므로 1 빼줘
                    return result  # 안전 거리 확정
                else:
                    visited[ni][nj] = visited[now[0]][now[1]]+1  # 방문 기록
                    Q.append((ni,nj))  # 큐에 추가해서 계속 탐색

    return result

max_ans = 0
for i in range(N):
    for j in range(M):
        if ocean[i][j] == 1:
            continue  # 상어가 있는 곳은 인접거리를 구할 필요 없으니 배제하기
        ans = bfs(i,j)  # bfs 탐색으로 해당 좌표의 인접거리를 읽어와서 ans에 담는다.
        if max_ans < ans:
            max_ans = ans

print(max_ans)