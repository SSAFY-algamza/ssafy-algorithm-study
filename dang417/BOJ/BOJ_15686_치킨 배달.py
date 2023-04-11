import sys
sys.stdin = open('input.txt')

from itertools import combinations

def calc_chicken_distance(chicken_lst):
    global result
    rlt = 0

    for home in home_lst:
        (i, j) = home
        tmp = 1e9
        for chicken in chicken_lst:
            (x, y) = chicken
            if tmp >= abs(i - x) + abs(j - y):
                tmp = abs(i - x) + abs(j - y)
        rlt += tmp

        if result < rlt:
            return

    if result >= rlt:
        result = rlt

# 집 리스트와 치킨집 리스트를 만든다
# 치킨집 리스트 중에서 M개를 선택한다
# 각 집에 대한 치킨거리를 계산한다
# 치킨 거리합의 최소값을 구한다

N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]
result = 1e9

home_lst = []
chicken_lst = []

for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            home_lst.append((i, j))
        elif city[i][j] == 2:
            chicken_lst.append((i, j))

M_choice = combinations(chicken_lst, M)

for chicken in M_choice:
    calc_chicken_distance(chicken)

print(result)