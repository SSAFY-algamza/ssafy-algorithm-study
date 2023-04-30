import sys
input = sys.stdin.readline

def find_parent(x):  # 인자로 들어온 노드의 부모노드를 찾아주는 함수
    if x != parent[x]:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union(x,y):  # 두 노드를 인자로 받아, 두 노드를 한 집합에 포함시켜주는 함수
    x_parent = find_parent(x)
    y_parent = find_parent(y)

    if x_parent < y_parent:
        parent[y_parent] = x_parent
    else:
        parent[x_parent] = y_parent

T = int(input())
for tc in range(1,T+1):
    print(F'Scenario {tc}:')

    users = int(input())  # 유저수
    parent = [i for i in range(users)]  # 부모노드 기록할 리스트
    relations = int(input())  # 관계수
    for _ in range(relations):  # 관계수만큼 반복
        A, B = map(int,input().split())
        union(A,B)
    m = int(input())
    for _ in range(m):
        A, B = map(int,input().split())
        A_root = find_parent(A)
        B_root = find_parent(B)
        if A_root == B_root:
            print(1)
        else:
            print(0)
    print()