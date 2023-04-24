import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
arr = sorted(map(int, input().split()))
GOOD = 0

for i in range(N):
    lst = arr[:i] + arr[i+1:]
    left ,right = 0, len(lst)-1

    while left < right:
        num = lst[left] + lst[right]
        if num == arr[i]:
            GOOD += 1
            break
            
        if num > arr[i] : right -= 1
        else : left += 1
print(GOOD)
