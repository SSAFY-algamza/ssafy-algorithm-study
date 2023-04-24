N = int(input())
M = int(input())
roots = [i for i in range(N+1)]  # 루트 노드 정보 저장할 배열
graph = [list(map(int,input().split())) for _ in range(M)]
graph.sort(key=lambda x:x[2])  # 가중치를 기준으로 정렬

def find_root(x):
    if roots[x] != x:
        roots[x] = find_root(roots[x])
    return roots[x]

answer = 0
for s, e, w in graph:
    sRoot = find_root(s)
    eRoot = find_root(e)
    if sRoot != eRoot:  # 루트노드가 서로 다르면, 즉 싸이클 형성이 안되면
        answer += w  # 트리에 포함시킬거고, answer에 거리 더해주기
        # 그리고 포함시켰으므로 둘 중 더 숫자가 작은 노드를 큰 노드의 부모 노드로 기록한다
        if sRoot < eRoot:
            roots[eRoot] = sRoot
        else:
            roots[sRoot] = eRoot

print(answer)