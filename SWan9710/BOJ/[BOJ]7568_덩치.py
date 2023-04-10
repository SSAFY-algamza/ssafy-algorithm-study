N = int(input())
arr = []
for i in range(N):
    kg, cm = map(int, input().split())
    arr.append((kg, cm))

# 나보다 덩치가 크다 = 키와 몸무게 둘다 나보다 크다
# 나보다 덩치가 큰사람의 수를 구해서
lst = []
for i in range(N):
    count = 1
    for j in range(N):
        if i == j:
            continue
        if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
            count += 1
    lst.append(count)
print(*lst)