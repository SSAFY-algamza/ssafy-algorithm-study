'''
동굴을 이차원 배열로 만들고, 각 좌표가 노드라고 생각하고 각 좌표마다 최소도둑루피를 기록한다.
각 칸에 있는 도둑루피의 크기는 일종의 가중치의 역할을 함
bfs로 움직여서 n-1 , n-1 좌표까지 탐색하는데, 탐색하면서 가져간 값이 적혀있는 값보다 작으면 갱신한다.
'''
import heapq

def dijkstra(x, y):
    Q = []
    heapq.heappush(Q,(cave[x][y],x,y))
    roopis[x][y] = cave[x][y]

    while Q:  # 큐가 있는 동안 반복
        now_total, i,j = heapq.heappop(Q)

        if now_total > roopis[i][j]:
            continue

        for di, dj in [(0,1),(0,-1),(1,0),(-1,0)]:
            ni = i + di
            nj = j + dj

            if 0 <= ni < N and 0 <= nj < N:
                next_total = now_total + cave[ni][nj]

                if roopis[ni][nj] > next_total:
                    roopis[ni][nj] = next_total
                    heapq.heappush(Q, (next_total, ni, nj))


cnt = 1
while 1:
    N = int(input())

    if N == 0:
        break

    cave = [list(map(int, input().split())) for _ in range(N)]
    roopis = [[float('inf')]*N for _ in range(N)]

    dijkstra(0, 0)
    print(f"Problem {cnt}:",roopis[N-1][N-1])
    cnt += 1
