'''
1. 추천받은 학생번호를 하나씩 가져와서
2. 사진틀에 이미 학생번호가 있으면 추천횟수를 늘려주고,
3. 사진틀에 해당 학생번호가 없으면 추가해준다.
(단, 이 때 사진틀이 가득찬 상황이면 추천횟수가 가장 적은 학생(1순위조건), 그 중에서도 과거에 게시된(2순위조건) 학생을
 빼고 추가해줘야한다)
4. 마지막에 사진틀에 남아있는 학생 번호를 증가하는 순서대로 출력
'''

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
            del_lst = sorted(candidates.items(), key=lambda x:(x[1][0],x[1][1]))
            del_key = del_lst[0][0]
            del(candidates[del_key])
        candidates[recommends[i]] = [1, i]  # 새로운 key를 생성. (횟수,등록순서) 튜플형태로 값을 저장. 횟수는 1로 초기화.

temp = sorted(candidates.keys())
for i in temp:
    print(i, end=" ")