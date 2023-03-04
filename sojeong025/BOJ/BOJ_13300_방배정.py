import sys
sys.stdin = open('input.txt')

# N 학생 수 / K 한 방에 배정할 수 있는 최대 인원
N, K = map(int, input().split())
girl = [0] * 7
boy = [0] * 7
for i in range(N):
    # S 성별 / Y 학년
    S, Y = map(int, input().split())

    if S == 1:
        boy[Y] += 1
    else:
        girl[Y] += 1

# print(boy)
# print(girl)

for i in range(1, 7):
    if boy[i] % K == 0:
        boy[i] = boy[i] // K
    else:
        boy[i] = boy[i] // K + 1

    if girl[i] % K == 0:
        girl[i] = girl[i] // K
    else:
        girl[i] = girl[i] // K + 1

print(sum(boy) + sum(girl))




