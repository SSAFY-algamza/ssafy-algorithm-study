'''
구현 아이디어
1. 배열을 오름차순으로 정렬
2. 반복문을 돌며 배열을 차례대로 1개씩 다 탐색
3. 그때 i 를 제외한 새로운 lst 에서 left, right 선택해서 두수의 합을 비교
4. 두 수의 합이 arr[i] 보다 크면 right 1 낮추기
5. 두 수의 합이 arr[i] 보다 작으면 left 1 올리기
6. 두 수의 합이 arr[i]와 같을경우 종료 good + 1
'''
import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
# 1. 배열 오름차순 정렬
arr.sort()
# 정답 저장할 공간
GOOD = 0

# 2. 반복문 돌며 배열 전체를 1씩 탐색하기
for i in range(N):

    # 3. i를 제외한 새로운 lst에서 left, right 선택
    lst = arr[:i] + arr[i+1:]
    left, right = 0, len(lst) - 1

    # 배열 탐색하는데 left가 right 보다 커지면 교차하는 순간이므로 배열범위 벗어남
    # 그 전까지 배열 탐색하며 left랑 right 위치 옮겨주기
    while left < right:
        num = lst[left] + lst[right]
        # 종료조건
        if num == arr[i]:
            GOOD += 1
            break

        # 4. 두 수의 합이 arr[i] 보다 큰 경우
        if num > arr[i]:
            right -= 1
        # 5. 두 수의 합이 arr[i] 보다 작은 경우
        else:
            left += 1
print(GOOD)