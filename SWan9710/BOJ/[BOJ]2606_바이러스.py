'''
컴퓨터수
연결된 컴퓨터수 입력받기
연결된 정보 배열에 저장
저장된 배열 깊이 우선 탐색 하면서 count 값 변경 시키기
'''
# 전체 컴퓨터 수
N = int(input())
# 컴퓨터끼리 연결된 정보
connected_computer = int(input())
# 연결된 컴퓨터 정보 저장할 배열
computed_array = [[] for _ in range(N+1)]
# 연결수를 세줄 count
count = 0
# 방문기록 확인용 배열
visited = [0] * (N+1)

# 연결정보 받기
for _ in range(connected_computer):
    computer_A, computer_B = map(int, input().split())
    # 양방향 연결
    computed_array[computer_A]+=[computer_B]
    computed_array[computer_B]+=[computer_A]

# 깊이우선탐색 실시
def DFS(now):
    global count
    visited[now] = 1
    for next in computed_array[now]:
        if visited[next] == 0:
            count += 1
            DFS(next)

DFS(1)
print(count)