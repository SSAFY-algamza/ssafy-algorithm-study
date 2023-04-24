N = int(input())
A, B = map(int, input().split())
M = int(input())
graph = [[] for i in range(N+1)]
for i in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)  # 양 방향이므로
    graph[y].append(x)  # 서로 인접노드로 추가한다
visited = [False] * (N+1)  # 이미 탐색한 곳을 기록해둘 배열
ans = 0  # 촌수계산할 변수를 0으로 초기화

def dfs(now,result):  # 첫번째 인자에는 현재 탐색하는 사람의 번호, 두번째 인자는 현재까지 계산한 촌수
    global ans

    if now == B:  # B에 도달하면 멈추고
        ans = result+1  # ans에 촌수를 할당하고 함수 끝
        return

    else:
        for i in graph[now]:  # 현재 사람의 인접노드를 순회
            if not visited[i]:
                visited[now] = True  # 방문기록
                dfs(i,result+1)  # 해당인접노드로 가서 다시 같은 방식으로 탐색

dfs(A,0)

if ans:
    print(ans-1)
else:
    print(-1)