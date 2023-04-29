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
parent = [i for i in range(N+1)]  # 인덱스는 노드 번호. 원소는 노드의 부모 노드를 기록.

for _ in range(N-2):
    A, B = map(int,input().split())
    union(A,B)

answer = []
for i in range(1,N+1):
    if i == parent[i]:  # 인덱스와 부모노드가 같은 노드만 정답리스트에 추가
        answer.append(i)
print(*answer)