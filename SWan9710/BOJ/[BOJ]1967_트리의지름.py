'''
트리의 지름을 구하기 위해
트리를 구성하고 해당 트리의 시작지점을 임의의 값으로 잡은 후 깊이우선탐색 실시
루트노드가 항상 1이므로 1에서 가장 먼곳까지의 길이를 구하면 반지름이 나옴
도착한 가장 먼 지점에서 다시 가장 먼지점까지의 거리를 구하면 지름이 됨

1. 트리구성
2. 루트에서 깊이우선탐색 실시해 가장 먼지점의 노드번호 알아내기
3. 해당 노드에서 다시 깊이우선 탐색 실시해 가중치 구해주기
'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

N = int(input())
# 0은 안쓰니 N+1 까지
graph = [[] for _ in range(N+1)]

# 1. 트리구성
for _ in range(N-1):
    parent, child, weight = map(int, input().split())
    # 무방향 그래프라서 부모 자식 둘다 추가
    graph[parent].append([child, weight])
    graph[child].append([parent, weight])

# 2. 루트에서 가장먼 지점까지의 노드를 구하는 깊이우선 탐색
# 2-1. 중복방문을 막기위해 방문체크 남기기
# 2-2. 루트에서 다음 노드로 방문시 아직 어디가 더 긴지 모르니 
# 가중치는 0으로 넘겨줘서 계산에 이상없게 해주기

def DFS(node, cost):    # 현재 노드, 현재 가중치
    for next_node, next_cost in graph[node]: # 다음 노드, 그때의 가중치
        # 방문기록 확인 후 방문한 적이 없다면
        # 해당 노드의 가중치를 현재의 가중치에 더해서 다시 DFS 실시
        if visited[next_node] == -1:
            visited[next_node] = cost + next_cost
            DFS(next_node, cost + next_cost)

# 방문기록 체크
visited = [-1] * (N+1)
visited[1] = 0
DFS(1, 0)

# 현재 visited에는 누적 가중치가 저장되어 있음
# 가장 큰 가중치를 가지는 node의 index번호 알아내기
# 그 index 번호에서 시작
start = visited.index(max(visited))

# 3. 현재의 노드에서 다시 DFS 실시
# 방문기록 초기화 및 가중치 초기화
visited = [-1] * (N+1)
visited[start] = 0
DFS(start, 0)

# visited 배열에는 누적가중치가 저장
# 이중 가장 큰 값을 출력
print(max(visited))