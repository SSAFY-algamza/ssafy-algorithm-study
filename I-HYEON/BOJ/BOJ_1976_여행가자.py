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

N = int(input())
parent = [i for i in range(N+1)]
M = int(input())
for i in range(N):
    temp = list(map(int,input().split()))
    for j in range(N):
        if temp[j] == 1:
            union(i+1,j+1)

plans = list(map(int,input().split()))

for i in range(M-1):
    A = find_parent(plans[i])
    B = find_parent(plans[i+1])

    if A != B:
        print('NO')
        break
else:
    print('YES')