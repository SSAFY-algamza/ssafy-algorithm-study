import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def DFS(start):
    # 트리에 저장된 1번째 관계부터 불러오기
    for i in tree[start]:
        # 초기 parents 는 전부 0으로 저장했으니 반복 돌면서 parents 저장해줌
        if parents[i] == 0:
            parents[i] = start
            DFS(i)

N = int(input())
# 관계를 저장할 tree
tree = [[] for _ in range(N+1)]

# tree의 부모찾기 위한 parents
parents = [0] * (N+1)

# 입력받은 관계 저장
for _ in range(N-1):
    x, y = map(int, input().split())
    tree[x].append(y)
    tree[y].append(x)

# 트리의 루트를 1로 정했으니 1로 DFS 탐색
DFS(1)

# 출력조건
# 각 노드의 부모 노드번호를 2번부터 순서대로 출력
for i in range(2, N+1):
    print(parents[i])