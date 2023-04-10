'''
구현 아이디어
1. 벽을 세우는건 백트래킹을 이용하여 배열 전체를 순환하며
    0인 곳에 벽을 세움
2. 벽을 3개 다 세우면 그때 bfs 실행
    벽을 세운 후의 배열을 이용하여 BFS 실행
    원본 배열을 해치면 DFS 끝났을때 세운 벽을 초기화 해야 하는데 원본이 바뀌면 결과가 바뀌므로
    리스트를 깊은복사 해야함 >> 리스트 슬라이싱 혹은 deepcopy
    슬라이싱은 복사안되서 deepcopy로 구현

3. bfs를 돌며 연구소에 바이러스 퍼트리기 => while문 사용
4. 모든곳에 바이러스가 퍼지고 더이상 바이러스가 퍼질 수 없을때
    0의 갯수 세주기
5. 결과를 저장할 값을 글로벌 공간에 작성 후 max 함수로 값을 비교하여 result 출력
'''
import sys
input = sys.stdin.readline
from collections import deque
import copy

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def BFS():
    global result

    virus = deque()
    arr = copy.deepcopy(arr_map)

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 2:
                virus.append((i, j))

    while virus:
        x, y = virus.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]

            if 0 <= nx < N and 0 <= ny < M:
                if arr[nx][ny] == 0:
                    arr[nx][ny] = 2
                    virus.append((nx, ny))

    count = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                count += 1
    result = max(result, count)

def DFS(n):
    # 종료조건
    if n == 3:
        BFS()
        return

    for i in range(N):
        for j in range(M):
            if arr_map[i][j] == 0:
                arr_map[i][j] = 1
                DFS(n + 1)
                arr_map[i][j] = 0

N, M = map(int, input().split())
arr_map = [list(map(int, input().split())) for _ in range(N)]
result = 0
DFS(0)
print(result)
'''
참고한 것
BFS를 실행할 때 인자를 아무것도 넘겨주지 않고도 실행이 가능하다
원본 배열만 이용하여 문제를 해결해 보려 하였는데 실패함
배열 2개를 이용한다는 아이디어 얻음
그 때 깊은복사를 위한 deepcopy 얻어옴
'''