import sys
input = sys.stdin.readline

def find_parent(x):  # 인자로 들어온 노드의 부모노드를 찾아주는 함수
    if x != parent[x]:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union(x,y):  # 두 노드를 인자로 받아, 두 노드를 한 집합에 포함시켜주는 함수
    x_parent = find_parent(x)
    y_parent = find_parent(y)

    if friend_fee[x_parent] < friend_fee[y_parent]:  # 친구비가 더 적은 노드를 택해야함
        parent[y_parent] = x_parent
    else:
        parent[x_parent] = y_parent

N, M, K = map(int,input().split())
friend_fee = [0]+list(map(int,input().split()))
parent = [i for i in range(N+1)]
for _ in range(M):
    A,B = map(int,input().split())
    union(A,B)

total = 0
for i in range(1,N+1):
    if i == parent[i]:
        total += friend_fee[i]

if K >= total:
    print(total)
else:
    print("Oh no")