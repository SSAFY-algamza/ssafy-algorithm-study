import sys
from heapq import heappush, heappop

# 값을 추가할 때 절대값과 일반값을 튜플로 묶어서 넣어주고
# 출력할때 절대값이 가장 작은 값을 출력
# 튜플값의 0 과 1중 1이 일반값 이므로 출력시 heap의 1번째 인자 출력
# 작성법 --> heappop(heap)[1] 으로 작성해 주어야 함
input = sys.stdin.readline

heap = []

N = int(input())
for _ in range(N):
    X = int(input())

    if X != 0:
        heappush(heap, (abs(X), X))
    else:
        if heap:
            print(heappop(heap)[1])
        else:
            print(0)