'''
N X N 크기의 농장
① 농장은 크기는 항상 홀수이다. (1 X 1, 3 X 3 … 49 X 49)
② 수확은 항상 농장의 크기에 딱 맞는 정사각형 마름모 형태로만 가능
'''
import sys
sys.stdin = open('2805_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    farm = [list(map(int, input())) for _ in range(N)]

    mid = N//2
    money = 0
    for i in range(N):
        if i <= mid:
            money += sum(farm[i][mid-i:mid+i+1])
        else:
            money += sum(farm[i][mid+i-N+1:mid-(i-N)])

    print(f'#{tc} {money}')


