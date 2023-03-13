import sys
sys.stdin = open('input.txt')

word = input().split('-')
w = []
for i in word:
    cnt = 0
    wo = i.split('+')
    for j in wo:
        cnt += int(j)
    w.append(cnt)

rd = w[0]
for i in range(1, len(w)):
    rd -= w[i]
print(rd)

