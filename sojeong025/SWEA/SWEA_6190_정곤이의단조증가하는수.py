'''
1 ≤ i < j ≤ N 인 두 i, j에 대해, Ai x Aj값이 단조 증가하는 수인 것들을 구하고
그 중의 최댓값을 출력하는 프로그램을 작성
'''

import sys
sys.stdin = open('6190_input.txt')

# 계산된 값이 단조 증가하는 수인지 확인하는 함수
def check(n):
    n = str(n)
    for i in range(len(n)-1):
        if n[i] > n[i+1]:
            return False
    return True


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    number = list(map(int, input().split()))

    max_num = -1
    for i in range(len(number)-1):
        for j in range(i+1, len(number)):
            two_num = number[i] * number[j]
            if max_num < two_num and check(two_num):
                max_num = two_num
    print(f'#{tc} {max_num}')