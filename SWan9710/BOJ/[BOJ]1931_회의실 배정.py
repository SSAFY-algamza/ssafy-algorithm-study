N = int(input())
meeting = [list(map(int, input().split())) for _ in range(N)]

# 시작시간을 기준으로 1번 정렬 후
# 종료시간을 기준으로 최종 정렬
# 만약 3 3 / 2 3 두개의 회의가 입력되는 경우 둘다 진행 가능하지만 3 3 을 먼저 확인하면
# 2 3 은 진행할 수 없다고 판단하기에 시작시간 먼저 정렬 후 종료시간을 기준으로 다시 정렬해주기
meeting.sort(key=lambda x: x[0])
meeting.sort(key=lambda x: x[1])

# 결과를 저장할 변수 와 시작시간을 비교해줄 time
result = 0
time = 0

for start, end in meeting:
    if time <= start:   # 회의실 배정 가능할때
        time = end
        result += 1

print(result)

