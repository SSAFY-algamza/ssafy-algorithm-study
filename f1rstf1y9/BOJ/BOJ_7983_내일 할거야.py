# 과제가 있을 때 내가 내일부터 연속으로 최대 며칠동안 놀 수 있는지
# d일이 걸리고 오늘로부터 t일 안에 끝내야 함
# 1–5일에는 놀고, 6–7일에는 1번째 과제를, 8–10일에는 3번째 과제를 한다. 11–12일에는 놀고, 13–13 일에 2번째 과제를 한다.
'''
3
2 8
1 13
3 10

5
'''
import sys
input = sys.stdin.readline
n = int(input())
homeworks = [tuple(map(int, input().split())) for _ in range(n)]
homeworks.sort(key=lambda x:(-x[1],x[0]))
# print(homeworks)
cur_day = homeworks[0][1]
for d, t in homeworks:
    if cur_day > t:
        cur_day = t-d
    else:
        cur_day -= d

print(cur_day)