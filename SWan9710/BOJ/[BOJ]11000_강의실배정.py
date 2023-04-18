'''
모든 수업을 들어야 한다 >> 종료시간 기준으로 정렬 필요없음
시간이 지나면 다른 강의실 개설하면 됨
강의실의 최소 사용갯수 구하기

구현 아이디어
1. 현재 회의 종료 시간보다 다음 회의 종료시간이 빠르면 회의실 추가개설
2. 현재 회의실에서 회의가 끝나는 시간보다 다음 회의 시작시간이 느리면 추가개설 X
'''
import sys
from heapq import heappush,heappop
input = sys.stdin.readline
N = int(input())

time = []
for _ in range(N):
    # 시작, 종료 입력받기
    si, ei = map(int, input().split())
    time.append([si, ei])

time.sort()
####################################
# print('----time----')
# print(time)
# print()
####################################
# 회의실 넣어줄거 생성
# 회의실의 첫번째 회의는 가장먼저 시작되는 회의
meeting = []
heappush(meeting, time[0][1])

for i in range(1, N):
    # 현재 회의가 종료 되지 않았을때 다음 회의가 시작되어야 하는경우
    # 회의실 추가개설
    if time[i][0] < meeting[0]:
        # 다음 회의의 종료시간으로 회의실 개설
        heappush(meeting, time[i][1])

    # 현재 회의가 종료되고 다음 회의가 시작되는 경우
    else:
        # 현재 회의가 끝났으니 방에서 빼주고
        # 다음회의의 종료시간으로 회의실 개설
        heappop(meeting)
        heappush(meeting, time[i][1])

# 개설된 회의실의 수
print(len(meeting))