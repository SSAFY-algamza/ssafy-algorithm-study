import sys
sys.stdin = open('input.txt')

# N : 보드의 크기 / color : 보드에 채워져 있는 사탕의 색상
# C 빨간색 P 파란색 Z 초록색 Y 노란색
N = int(input())
color = [list(input()) for _ in range(N)]

max_candy = 0


