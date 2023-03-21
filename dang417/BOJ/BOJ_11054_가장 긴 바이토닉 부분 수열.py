import sys
sys.stdin = open('input.txt')

'''
수열 S가 어떤 수 Sk를 기준으로
S1 < S2 < ... < Sk-1 < Sk > Sk+1 > ... > SN-1> SN
을 만족한다면 바이토닉 수열
부분 수열 중 바이토닉 수열이면서 가장 긴 수열의 길이를 구하는 프로그램
1. 부분 수열을 구하기
1-1 바이토닉이 아님이 확인 될 경우 백트래킹
1-2 수열의 길이 구하기

한 수를 기준으로 가장 긴 증가하는 수열과 가장 긴 감소하는 수열 검색
바이토닉 수열의 경우 그 수가 반드시 최댓값이어야 할 것이므로 최댓값인 경우에만 탐색
'''

N = int(input())
A = list(map(int, input().split()))
dp = [1] * N

for i in range(1, N):
    for j in range(i):
        if A[j] < A[i]:
            dp[i] = max(dp[i], dp[j] + 1)

for i in range(1, N):
    for j in range(i):
        if A[j] > A[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))