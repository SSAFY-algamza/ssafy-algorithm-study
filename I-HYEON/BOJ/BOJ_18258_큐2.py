'''
-> 문제정보
큐를 구현한 다음, 입력으로 주어지는 명령을 처리해 출력

-> 아이디어-
0. T로 명령어 개수를 입력받고 그만큼 반복한다.
1. push의 경우 주어지는 정수x까지 입력받아야 함 -> try, except로 구분해서 다른 케이스와 구분
(try, except안쓰고 할 수 있는 방법없을까..)
2. 명령어에 따라 if구문을 나누어서 작성해주면 끝
'''
from collections import deque
import sys

T = int(input())
Q = deque([])
input = sys.stdin.readline

for i in range(T):
    inp_str = input().split()
    order = inp_str[0]
    if order == 'push':
        Q.append(inp_str[1])
    elif order == 'front':
        if Q:
            print(Q[0])
        else:
            print(-1)
    elif order == 'back':
        if Q:
            print(Q[-1])
        else:
            print(-1)
    elif order == 'size':
        print(len(Q))
    elif order == 'pop':
        if Q:
            temp = Q.popleft()
        else:
            temp = -1
        print(temp)
    elif order == 'empty':
        if Q:
            print(0)
        else:
            print(1)