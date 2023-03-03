import sys
sys.stdin = open('input.txt')

from collections import deque


def BFS(N):
    queue = deque([])
    queue.append(N)
    while queue:
        x = queue.popleft()
        if x == K:
            print(second[x])
            break
        else:
            for nx in (x-1, x+1, 2*x):
                if 0 <= nx <= 100000 and second[nx] == 0:
                    second[nx] = second[x] + 1
                    queue.append(nx)


# N이 수빈 위치 K가 동생 위치
N, K = map(int, input().split())
second = [0] * 100001

BFS(N)

