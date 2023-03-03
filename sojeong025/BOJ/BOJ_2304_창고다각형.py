import sys
sys.stdin = open('input.txt')

N = int(input())
L_H = []
for i in range(N):
    # L x축 위치 H 높이
    L, H = map(int, input().split())
    L_H.append([L, H])

# 만약 index 1번 기준으로 정렬한다면,
# L_H.sort(key=lambda L_H: L_H[1])
L_H.sort()
print(L_H)

# 가장 높은 기둥 번호 / 그 인덱스 찾기
high = 0
high_idx = 0
cnt = 0
for i in L_H:

    if i[1] > high:
        high = i[1]
        high_idx += cnt
        cnt = 0
    cnt += 1

# 초기 높이
start = L_H[0][1]
container = high
# 앞에서부터 최대 높이까지 반복
for i in range(high_idx):
    if start < L_H[i+1][1]:
        container += start * (L_H[i+1][0] - L_H[i][0])
        start = L_H[i+1][1]
    else:
        container += start * (L_H[i+1][0] - L_H[i][0])
# 뒤에서부터 최대 높이까지 반복
start = L_H[-1][1]
for i in range(N-1, high_idx, -1):
    if start < L_H[i-1][1]:
        container += start * (L_H[i][0]-L_H[i-1][0])
        start = L_H[i-1][1]
    else:
        container += start * (L_H[i][0]-L_H[i-1][0])

print(container)