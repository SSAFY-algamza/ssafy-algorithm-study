import sys
input = sys.stdin.readline

n, m = map(int,input().split())
parent = [i for i in range(n+1)]  # 모든 노드의 부모노드를 기록할 리스트. 초기화는 자기자신.

def find(x):  # 해당 노드의 부모노드를 찾아주는 함수
    while x != parent[x]:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return parent[x]


def union(a,b):  # 두 노드의 집합을 합치는 함수
    a = find(a)  # 부모를 찾아와서 할당
    b = find(b)  # 부모를 찾아와서 할당
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for _ in range(m):
    isUnionOrFind, a, b = map(int,input().split())

    if isUnionOrFind:
        if find(a) == find(b):  # 만약 1이라면 두 원소가 같은 집합에 포함되어있는지 확인
            print("YES")
            continue
        else:
            print("NO")
            continue
    else:
        union(a,b)  # 만약 0이라면 두 원소를 같은 집합에 속하도록 합집합 연산을 수행한다.