N = int(input())
lst = list(map(int, input().split()))

lst.sort()  # 크기 순으로 정렬한다

Good = 0

for i in range(N):
    left = 0
    right = N-1

    while left < right:
        if left == i:
            left += 1
            continue
        if right == i:
            right -= 1
            continue

        summ = lst[left] + lst[right]

        if summ == lst[i]:
            Good += 1
            break
        elif summ < lst[i]:
            left += 1
        else:
            right -= 1

print(Good)