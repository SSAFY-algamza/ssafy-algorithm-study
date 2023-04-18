'''
노드의 수
간선의 수
간선당 연결 비용 및 연결 정보

순으로 주어짐
컴퓨터와 컴퓨터를 직접 연결해야 함
처음부터 끝까지 연결해야 하는데 중간에 싸이클이 생기면 무한 루프를 돌기 때문에 싸이클 없이
끝까지 컴퓨터를 연결해야 하는데
그 중 최소의 비용을 가지는 연결을 구하라
'''

def find_parents(n):
    # 자기 자신이 부모가 아닌경우
    if parents[n] != n:
        # 현재 입력받은 n의 부모에 해당하는 노드의 부모를 찾으러 감
        # 즉 부모의 부모를 찾으러 감
        parents[n] = find_parents(parents[n])
    return parents[n]

def union(a, b):
    # 현재 a, b에 대한 부모를 먼저 찾아옴
    a = find_parents(a)
    b = find_parents(b)

    # 부모를 하나의 부모로 합쳐주기
    # 보통 트리를 그릴때 더 작은 값이 위에 있으므로 더 작은 값으로 부모를 초기화 해줄거
    if a < b:
        parents[b] = a
    else:
        parents[a] = b

V = int(input())
E = int(input())
# 간선의 연결정보 edgds
edges = [list(map(int, input().split())) for _ in range(E)]

# 최소 비용 순으로 오름차순 정렬
edges.sort(key=lambda x : x[2])
# 최초 부모 노드들은 자기 자신으로 정의
parents = [i for i in range(V+1)]

total_cost = 0
for edge in edges:
    a, b, cost = edge
    # 서로의 부모가 다른경우 싸이클 발생 X, 서로의 부모를 동일하게 만들기 > 트리 연결 작업
    if find_parents(a) != find_parents(b):
        union(a, b)
        # edges는 이미 최소비용 순으로 오름차순 정렬해둠
        # 부모가 서로 다른 경우 다리가 싸이클이 발생하지 않는 최소 비용이므로
        # 그 때의 비용을 최종 결과에 더해줌
        total_cost += cost

print(total_cost)