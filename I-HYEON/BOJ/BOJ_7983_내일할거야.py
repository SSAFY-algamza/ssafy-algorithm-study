import sys
input = sys.stdin.readline

N = int(input())
homework_info = [list(map(int,input().split())) for _ in range(N)]

homework_info.sort(reverse=True, key=lambda x:x[1])  # 마감기한을 기준으로 내림차순으로 정렬한다

now = max(homework_info,key=lambda x:x[1])[1]  # 제일 늦은 마감기한을 기준으로 거꾸로 세어나갈 예쩡
for i,j in homework_info:  # 튜플을 하나씩 가져와서
    now = min(now,j)  # 일단 마감기한은 지켜야 하니까, 현재 가리키고 있는 날과 마감기한 중 더 이른 쪽을 택해서 now를 갱신
    now -= i  # 거기서 과제를 하는 날을 확보해야하니까 i(과제하는데 걸리는날)만큼 차감

print(now)  # 마지막에 남은 날이 연속으로 쉴 수 있는 최대 일수가 된다