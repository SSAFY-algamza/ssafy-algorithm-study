import sys
from heapq import heappush, heappop, heapify
input = sys.stdin.readline

N, M = map(int, input().split())
heap = list(map(int, input().split()))

# heap 자료형으로 변환해주는 heapify
heapify(heap)
count = 0

for _ in range(M):
    count += heappop(heap)
    count += heappop(heap)
    heappush(heap, count)
    heappush(heap, count)
    count = 0

print(sum(heap))