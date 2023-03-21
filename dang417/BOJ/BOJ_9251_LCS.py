import sys
sys.stdin = open('input.txt')

'''
1. Longest Common Substring
    연속되는 공통 문자열을 찾는 경우 만약 현재의 문자열과 비교하는 문자열이 같다면,
    현재의 문자열 이전과 비교하는 문자열 이전의 문자열들까지의 공통 부분의 길이 + 1 이므로
    DP[i][j] = DP[i-1][j-1] + 1
    
    아닌 경우, 공통 부분이 연속되지 않으니 길이를 초기화 (= 0)

2. Longest Common Subsequence
    Longest Common Substring과 다른 점은, 부분 수열의 길이를 재는 것이기 때문에
    1) 만약 연속되지 않는다고 하더라도 공통 부분의 길이를 초기화 하지 않고 유지해 주어야 한다.
    2) 유지해 줄 경우 현재의 문자열 또는 비교하는 문자열이 기준이 되어야 하므로, 초기화 시에
    DP[i][j] = max(DP[i-1][j], DP[i][j-1])로써 공통 부분의 길이를 유지
    
    만약 현재의 문자열과 비교하는 문자열의 길이가 같은 경우, 동일하게
    DP[i][j] = DP[i-1][j-1] + 1 로 처리한다.
'''

A = input()
B = input()
DP = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]

for i in range(1, len(A) + 1):
    for j in range(1, len(B) + 1):
        if A[i-1] == B[j-1]:
            DP[i][j] = DP[i-1][j-1] + 1
        else:
            DP[i][j] = max(DP[i-1][j], DP[i][j-1])

print(DP[-1][-1])
