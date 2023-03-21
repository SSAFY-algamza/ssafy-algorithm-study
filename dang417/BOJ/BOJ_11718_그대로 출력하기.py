import sys
sys.stdin = open('input.txt')

S = sys.stdin.read().split('\n')
for i in range(len(S)):
    print(S[i])
