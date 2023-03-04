import sys
sys.stdin = open('input.txt')

from collections import deque


def BFS(N):
    queue = deque()
    queue.append(N)
    while queue:
        x = queue.popleft()
        if x == K:
            print(second[x])
            break
        else:
            for nx in (2*x, x-1, x+1):
                if 0 > nx or nx > 100000:
                    continue
                if second[nx] == 0:
                    if nx == 2*x and visited[nx] == 0:
                        second[nx] = second[x]
                        visited[nx] = 1
                        # 우선순위 먼저 담을 때 -> appendleft() 사용
                        queue.appendleft(nx)
                    else:
                        if visited[nx] == 0:
                            second[nx] = second[x] + 1
                            visited[nx] = 1
                            queue.append(nx)

N, K = map(int, input().split())
second = [0] * 100001
visited = [0] * 100001
BFS(N)