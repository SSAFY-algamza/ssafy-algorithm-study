import sys
sys.stdin = open("input.in", "r")

N = int(input())
M = int(input())
recommends = list(map(int, input().split()))

# dictionary 생성(크기 N을 유지할 예정)
candidates = dict()

for i in range(M):  # 추천 리스트를 순회하면서 한 명씩 가져온다

    if recommends[i] in candidates.keys():  # 해당 후보가 이미 존재하면
        candidates[recommends[i]][0] += 1  # 추천 횟수를 올려주고

    else:
        if len(candidates) >= N:  # 사진틀이 full 상태일 때
            del_lst = sorted(candidates.items(),key=lambda x:(x[1][0],x[1][1]))
            del_key = del_lst[0][0]
            del(candidates[del_key])
        candidates[recommends[i]] = [1, i]  # 새로운 key를 생성. (횟수,등록순서) 튜플형태로 값을 저장. 횟수는 1로 초기화.

temp = sorted(candidates.keys())
for i in temp:
    print(i, end=" ")