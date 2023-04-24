import heapq
import sys
input = sys.stdin.readline
N = int(input())
lst = []

for _ in range(N):
    num = int(input())
    if num > 0:
        heapq.heappush(lst, -num)
    elif num == 0:
        if not lst:
            print(0)
        else:
            print(-heapq.heappop(lst))