import sys
sys.stdin = open('input.txt')

# N 가로 M 세로
N, M = map(int, input().split())
store_num = int(input())
location = []
for _ in range(store_num + 1):
    dir, dis = map(int, input().split())
    if dir == 1:    # 북
        location.append([dis, M])
    elif dir == 2:  # 남
        location.append([dis, 0])
    elif dir == 3:  # 서
        location.append([0, M-dis])
    elif dir == 4:  # 동
        location.append([N, M-dis])

dong = location.pop()   # 동근이 현재 위치
length = 0

for i in location:
    if dong[1] == 0 or dong[1] == M:    # 동근 위치가 남이나 북이면
        if i[1] == 0 or i[1] == M:      # 상점도 남이나 북이면
            if dong[1] == i[1]:
                length += abs(i[0] - dong[0])
            elif dong[1] != i[1]:
                length += min(dong[0] + M + i[0], N - dong[0] + M + N - i[0])
        elif i[0] == 0 or i[0] == N:    # 상점이 서나 동이면
            if dong[1] == M:    # 동근이 북
                if i[0] == 0:    # 상점이 서
                    length += dong[0] + M - i[1]
                elif i[0] == N:     # 상점이 동
                    length += N - dong[0] + M - i[1]
            if dong[1] == 0:
                if i[0] == 0:  # 상점이 서
                    length += i[1] + dong[0]
                elif i[0] == N:  # 상점이 동
                    length += i[1] + N - dong[0]

    elif dong[0] == 0 or dong[0] == N:  # 동근 위치가 서나 동이면
        if i[0] == 0 or i[0] == N:  # 상점도 서나 동이면
            if dong[0] == i[0]:
                length += abs(i[1] - dong[1])
            elif dong[0] != i[0]:
                length += min(dong[1] + N + i[1], M - dong[1] + N + M - i[1])
        elif i[1] == 0 or i[1] == M:   # 상점이 남 북이면
            if dong[0] == 0:    # 동근이 서
                if i[1] == 0:   # 상점이 남
                    length += dong[1] + i[0]
                elif i[1] == M:     # 상점이 북
                    length += M - dong[1] + i[0]
            elif dong[0] == N:  # 동근이 동
                if i[1] == 0:   # 상점이 남
                    length += dong[1] + N - i[0]
                elif i[1] == M:     # 상점이 북
                    length += M - dong[1] + N - i[0]
print(length)
