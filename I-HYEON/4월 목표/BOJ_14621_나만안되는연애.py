import sys
sys.stdin = open("input.in", "r")

N, M = map(int, input().split())
colleges = list(input().split())
lst = [list(map(int, input().split())) for _ in range(M)]
lst.sort(key=lambda x: x[2])
root_node = [i for i in range(N+1)]

def find(x):
    if x != root_node[x]:
        root_node[x] = find(root_node[x])
    return root_node[x]

num = 0
answer = 0
for s, e, w in lst:
    sRoot = find(s)
    eRoot = find(e)
    if sRoot != eRoot and colleges[s-1] != colleges[e-1]:
        if sRoot > eRoot:
            root_node[sRoot] = eRoot
        else:
            root_node[eRoot] = sRoot
        answer += w
        num += 1

if num == N-1:
    print(answer)
else:
    print(-1)