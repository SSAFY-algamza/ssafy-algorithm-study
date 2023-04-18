import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

N = int(input().rstrip())
A = sorted(list(map(int, input().rstrip().split())))
rlt = 0


for i in range(N):
    tmp = A[:i] + A[i+1:]
    left, right = 0, N-2
    while left < right:
        cand = tmp[left] + tmp[right]
        if cand == A[i]:
            rlt += 1
            break
        if cand < A[i]: left += 1
        else: right -= 1

print(rlt)