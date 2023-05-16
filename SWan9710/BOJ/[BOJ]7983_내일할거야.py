# 과제의 갯수
N = int(input())
homework = [list(map(int, input().split())) for _ in range(N)]
# 마감일 기준으로 오름차순 정렬
# 제출일이 가장 마지막날을 가장 마지막에 제출
homework.sort(key=lambda x:x[1], reverse=True)

# 과제제출까지 남은시간
restTime = homework[0][1]

# 현재 마감일과 과제수행하며 남은 마감일중 더 작은 날짜에 소요시간을 빼줌
# 끝까지 반복
for i in range(N):
    restTime = min(homework[i][1], restTime) - homework[i][0]

# 마지막 과제에서 처음 과제까지 제출하고 처음 과제를 제출하기 전이 가장 긴 휴식시간이 됨
print(restTime)