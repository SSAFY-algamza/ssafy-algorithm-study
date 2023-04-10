import sys

input = sys.stdin.readline
from heapq import heappush, heappop
# heapq 에는 최대값을 출력해주는 방법 따로 존재 X
# heappush 할때 들어가는 값을 음수로 저장해주면 제일 큰 수에 -가 붙으니
# 해당수가 제일 작은 수가 되서 heap에 제일 앞에 위치하게 된다.
# 이때 출력시 -를 붙여서 출력해주면 제일 작은수(ex -5)를 다시 -를 붙여서 출력해주면
# 최대값을 얻을 수 있다.

arr = []

N = int(input())
for _ in range(N):
    X = int(input())

    if X != 0:
        heappush(arr, -X)
    else:
        if arr:
            print(-heappop(arr))
        else:
            print(0)