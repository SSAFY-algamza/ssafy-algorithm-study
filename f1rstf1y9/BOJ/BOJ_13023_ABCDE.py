import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def bt(n, cnt):
    if cnt == 5:
        return True
    for i in friends[n]:
        if not visited[i]:
            visited[i] = 1
            if bt(i, cnt+1):
                return True
            visited[i] = 0
    return False


N, M = map(int, input().split())
friends = [[] for _ in range(N)]
isValid = False
for _ in range(M):
    a, b = map(int, input().split())
    friends[a].append(b)
    friends[b].append(a)

for i in range(N):
    visited = [0]*N
    visited[i] = 1
    if bt(i, 1):
        isValid = True
        break

print(1 if isValid else 0)
