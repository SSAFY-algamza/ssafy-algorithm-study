from collections import deque

N, M, V = map(int,input().split())

adj = [[] for _ in range(N+1)]  # 정점의 개수마다 인접리스트를 만들거고, 인덱스 맞춰주려고 +1
for _ in range(M) :
    a, b = map(int, input().split())
    adj[a].append(b)  # a 번 노드에도 b를 추가해주고
    adj[b].append(a)  # b 번 노드에도 a를 추가해주자

for i in range(1, N+1):
    adj[i].sort()

dfs_visited = [0]*(N+1)
bfs_visited = [0]*(N+1)
dfs_ans = []
bfs_ans = []
def DFS(start):  # DFS 함수
    dfs_visited[start] = 1
    print(start,end=" ")

    for i in adj[start]:
        if not dfs_visited[i]:
            DFS(i) # 이 아래에 return을 붙이면 안되는 이유가 뭐지??????

def BFS(start):  # BFS 함수

    Q = deque([])  # 빈큐를 만들고
    Q.append(start)  # 첫정점을 집어넣는다

    while Q:  # 반복문을 돈다
        now = Q.popleft()  # 큐의 가장 앞 원소를 빼서
        print(now,end=" ")
        bfs_visited[now] = 1

        for i in adj[now]:  # 해당 정점의 인접 리스트를 돌면서
            if not bfs_visited[i]:  # 방문하지 않은 정점은
                bfs_visited[i] = 1  # 미리 방문 표시해주고
                Q.append(i)  #  일단 큐에 다 담는다
    return


DFS(V)
print()
BFS(V)