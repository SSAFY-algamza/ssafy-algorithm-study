'''
1. 외부 접촉되는 부분만 치즈가 녹음 > BFS 탐색할때 0으로 돌아서 1을 만났을때 녹여주기
2. 외부 테두리가 0으로 주어지기 때문에 0,0 에서 시작
3. BFS를 돌며 없어지는 치즈의 개수를 카운트 하고 반환값으로 넘겨주기
3-1. 치즈의 개수를 이용하여 반복문을 종료시키는 지점으로 이용
4. 결과값 저장 후 문제에 주어지는 원하는 시간에 해당하는 결과 출력
'''
import sys
from collections import deque
input = sys.stdin.readline

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def BFS():
    # 방문표시배열
    visited = [[0] * M for _ in range(N)]
    queue = deque()
    # 시작지점은 항상 0,0 >> 외부가 0으로 둘러싸져 있기때문
    queue.append([0,0])
    visited[0][0] = 1   # 방문표시
    # 녹은 치즈의 갯수세기 위한 count
    count = 0
    while queue:
        sx, sy = queue.popleft()

        for k in range(4):
            nx, ny = sx + dx[k], sy + dy[k]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                # 방문한 곳이 외부공기 부분이면
                if cheeze[nx][ny] == 0:
                    # 중복방문 없애기 위해 방문체크 후 다음 시작지점으로 queue에 넘겨주기
                    visited[nx][ny] = 1
                    queue.append([nx, ny])

                # 치즈를 만난경우
                elif cheeze[nx][ny] == 1:
                    # 해당부분을 녹이는 거니 0으로 바꿔주고 녹인갯수 + 1
                    cheeze[nx][ny] = 0
                    count += 1
                    # 방문처리
                    visited[nx][ny] = 1
    # while 문 다 돈경우 >> 배열의 끝까지 탐색한 경우
    # 이때 녹인 치즈의 갯수 result에 넣어주기
    result.append(count)
    # 녹인 치즈의 수 반환
    return count


N, M = map(int, input().split())
cheeze = [list(map(int, input().split())) for _ in range(N)]
result = []

# 시작하는 시간
time = 0
while True:
    time += 1
    # 녹인 치즈의 갯수를 BFS 탐색하여 얻은 치즈의 갯수로 재할당
    count = BFS()
    # 만약 0인경우 모든 치즈가 녹은 경우이니 더이상 반복할 필요 없으므로 종료
    if count == 0:
        break

# break 걸리기 전에 이미 time 은 +1 해주니 결과 출력시 -1 해주기
print(time-1)

# 결과에 저장되는 녹은 치즈의 갯수 중 녹기 한시간 전은 배열의 마지막 앞
print(result[-2])