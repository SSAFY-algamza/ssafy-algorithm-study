N, M = map(int, input().split())
# 비가 고일수 있는 기둥의 높이
rain = list(map(int, input().split()))

result = 0
# 기둥의 양 끝에는 빗물이 고일 수 없으니 중간부분만 계산
for i in range(1, M-1):
    # 내 위치를 기준으로 양옆에 가장 높은 기둥을 들고옴

    left = max(rain[:i])
    right = max(rain[i+1:])

    # 그 중 더 낮은 기둥의 높이만큼 물이 고일 수 있으니 두 기둥중 더 낮은값 선택
    count = min(left, right)

    # 선택한 값이 내 위치보다 더 높은경우 그 차이만큼 빗물이 고일 수 있음
    # 만약 내가 양옆 기둥보다 더 높다면 빗물이 고일 수 없음
    if rain[i] < count:
        result += count - rain[i]

print(result)