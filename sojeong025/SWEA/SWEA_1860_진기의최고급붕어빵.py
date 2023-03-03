'''
0초부터 붕어빵을 만들기 시작하며, M초의 시간을 들이면 K개의 붕어빵을 만들 수 있다.
붕어빵이 완성되면 어떤 시간 지연도 없이 다음 붕어빵 만들기를 시작할 수 있다
0초 이후에 손님들이 언제 도착하는지 주어지면, 모든 손님들에게 기다리는 시간없이 붕어빵을 제공할 수 있는지 판별하는 프로그램
'''

import sys
sys.stdin = open('1860_input.txt')

T = int(input())
for tc in range(1, T+1):
    # 자격을 얻은 N명의 사람 / M초의 시간으로 K개의 붕어빵 만들 수
    N, M, K = map(int, input().split())
    # 각 사람들의 도착시간 오름차순으로 정렬
    arrive_second = list(map(int, input().split()))
    arrive_second.sort()

    # 결과값 담을 곳
    result = ''
    for i in range(N):
        # 붕어빵 식 중요!!
        fish = (arrive_second[i] // M) * K - (i+1)
        if fish >= 0:
            result = 'Possible'
        else:
            result = 'Impossible'
            break

    print(f'#{tc} {result}')




