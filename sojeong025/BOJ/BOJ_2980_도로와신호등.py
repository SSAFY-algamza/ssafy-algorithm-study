import sys
sys.stdin = open('input.txt')

# 신호등 빨간불 지속되는 시간 초록 불 지속되는 시간
# 첨엔 모두 빨간색이고 상근이 1초에 1미터 이동
# 색상 빨간색이면 멈추고 초록색으로 바뀔때까지 기다림 - 이동시간 구하기

# N 신호등 개수 L 도로 길이
N, L = map(int, input().split())
second = 0
now = 0
for _ in range(N):
    # D 신호등의 위치  R 빨간색 G 초록색 - 지속시간
    D, R, G = map(int, input().split())

    second += (D - now)
    now = D
    if second % (R + G) <= R:
        second += (R - second % (R+G))

second += (L - now)
print(second)





