from itertools import combinations
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range (n)]

# 0은 빈 칸, 1은 집, 2는 치킨집
# 치킨집 개수 최대 M개 고르고 나머지 폐업 -> 어떻게 고르면 도시 치킨 거리가 가장 작게 될지

# m개 치키집 선택하는 모든 조합에 대해 도시 치킨 거리 구하기 => abs(r1-r2) + abs(c1-c2)
# 집과 치킨집의 좌표를 각각 리스트에 저장 => itertools의 combinations 이용해 치킨집 리스트 chick에서 m개 선택하고 치킨 거리 구하기

res = 999999
house = [] # 집 좌표
chick = [] # 치킨집 좌표

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            house.append([i, j])
        elif arr[i][j] == 2:
            chick.append([i, j])

for chi in combinations(chick, m): # m개 치킨집 고르기
    temp = 0 # 도시의 치킨 거리
    for h in house:
        chi_len = 999 # 각 집마다 치킨 거리
        for j in range(m):
            chi_len = min(chi_len, abs(h[0]-chi[j][0]) + abs(h[1]-chi[j][1]))
        temp += chi_len
    res = min(res,temp)

print(res)