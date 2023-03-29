'''
부모와 자식의 관계를 이용하여 dfs 를 돌며 촌수를 계산해 결과 리스트에 더하는 방식
1. 부모와 자식의 관계를 이용하여 relation 리스트 만들어주기
2. dfs 탐색하며 재귀함수로 촌수 작성하기
3. 방문표시 남기기 위한 visited 리스트 작성하기
4. 촌수를 표시할 결과 리스트 작성하기
visited를 그대로 이용하여 결과를 작성할때 reltions에 여러개의 값이 들어가는 경우
결과값이 다르게 출력됨
촌수를 계산해서 저장할 새로운 리스트 필요
'''

def DFS(start):
    visited[start] = 1
    for i in relations[start]:
        if not visited[i]:
            result[i] = result[start] + 1
            DFS(i)

N = int(input())
# 계산해야 하는 사람의 번호
first, second = map(int, input().split())
# 부모와 자식들 간의 관계의 개수 M
M = int(input())
# 부모와 자식의 관계를 넣을 리스트
# 0은 안쓰니까 1부터 N 까지 만들어주기
relations = [[] for _ in range(N+1)]
# 마찬가지로 0은 안쓰니까 1부터 N + 1까지
visited = [0] * (N+1)
result = [0] * (N+1)

# 부모 자식의 관계를 relation에 넣어줌
for i in range(M):
    p, c = map(int, input().split())
    relations[p].append(c)
    relations[c].append(p)
# print(relations)

DFS(first)
if result[second] > 0:
    print(result[second])
else:
    print(-1)

