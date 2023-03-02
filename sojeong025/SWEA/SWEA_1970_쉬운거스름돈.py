'''
손님에게 거슬러 주어야 할 금액 N이 입력되면
돈의 최소 개수로 거슬러 주기 위하여 각 종류의 돈이 몇 개씩 필요한지 출력
'''

import sys
sys.stdin = open('1970_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())  # 거슬러 주어야 할 금액
    # 마켓에서 사용하는 돈의 종류
    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    # 각 돈의 종류마다 필요한 개수
    need = [0] * 8

    # 전체 종류 8개를 돌며,
    for i in range(8):
        # 거슬러 주어야 할 금액을 제일 단위가 큰 돈부터 나누어 0이 아닐 때까지 반복
        if N // money[i] != 0:
            need[i] = N // money[i]
            # N은 단위가 큰 돈부터 나눈 나머지로 계속 재할당
            N = N % money[i]

    print(f'#{tc}')
    print(*need)



