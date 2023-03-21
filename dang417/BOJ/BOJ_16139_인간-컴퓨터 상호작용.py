import sys
sys.stdin = open('input.txt')

'''
각 문자 별로 해당하는 인덱스 까지의 누적합을 구해놓고
입력 받으면서 출력
'''

S = input()
q = int(input())
prefix_sum = [[0] * (len(S)) for _ in range(26)]

prefix_sum[ord(S[0])-97][0] = 1

for i in range(1, len(S)):
    prefix_sum[ord(S[i])-97][i] = 1
    for j in range(26):
        prefix_sum[j][i] += prefix_sum[j][i-1]

for _ in range(q):
    a, l, r = input().split()
    l, r = map(int, (l, r))
    if l == 0:
        print(prefix_sum[ord(a) - 97][r])
        continue
    else:
        print(prefix_sum[ord(a) - 97][r] - prefix_sum[ord(a) - 97][l-1])
