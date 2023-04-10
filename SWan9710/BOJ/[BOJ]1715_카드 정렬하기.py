import sys
from heapq import heappush, heappop, heapify
input = sys.stdin.readline

heap = []
N = int(input())
for _ in range(N):
    card = int(input())
    heappush(heap, card)

result = 0
count = 0

while len(heap) > 1:
    count += heappop(heap)
    count += heappop(heap)
    heappush(heap, count)
    result += count
    count = 0

print(result)
