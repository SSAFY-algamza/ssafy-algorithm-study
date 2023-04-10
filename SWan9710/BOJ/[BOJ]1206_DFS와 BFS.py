import sys
sys.setrecursionlimit(10**6)

# DFS 탐색
def DFS(start):
    # 방문기록 표시
    visited_1[start] = 1

    # 방문 기록 표시후 할일?
    # 정점번호 출력하기
    print(start, end=' ')

    # DFS 탐색시 배열을 순서대로 탐색 시작할 번호가 주어지므로 그 배열부터 탐색 시작
    for i in relation[start]:

        # 방문기록이 없다면 DFS 실시
        if not visited_1[i]:
            DFS(i)

# BFS 탐색
def BFS(start):
    # q에 시작 정점 저장
    queue = [start]

    # 방문표시
    visited_2[start] = 1

    # queue에 값이 있을때
    while queue:

        # v 값 뽑아오기 그 후 할일?
        # 정점번호 출력하기
        v = queue.pop(0)
        print(v, end=' ')

        # 재귀함수가 아니므로 queue에 새로운 정점번호를 append 하는 형식으로 저장 및 불러오기
        for i in relation[v]:
            if not visited_2[i]:
                visited_2[i] = 1
                queue.append(i)

# 정점갯수, 간선갯수, 정점번호
N, M, V = map(int, input().split())

# 관계를 저장할 배열
relation = [[] for _ in range(N + 1)]
# DFS 와 BFS용 배열
visited_1 = [0] * (N + 1)
visited_2 = [0] * (N + 1)

# 관계 저장
for i in range(M):
    p, c = map(int, input().split())
    relation[p].append(c)
    relation[c].append(p)
# print(relation)

# V 부터 방문된 점을 순서대로 출력하기 위해 탐색을 위한 배열 정렬
for i in relation:
    i.sort()
    # print(i)
    # print('-' * 30)

DFS(V)
print()
BFS(V)