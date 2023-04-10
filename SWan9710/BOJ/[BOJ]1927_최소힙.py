import sys
input = sys.stdin.readline
from heapq import heappush, heappop

heap = []
N = int(input())
for _ in range(N):
    X = int(input())
    if X != 0:
        heappush(heap, X)
    else:
        if heap:
            print(heappop(heap))
        else:
            print(0)