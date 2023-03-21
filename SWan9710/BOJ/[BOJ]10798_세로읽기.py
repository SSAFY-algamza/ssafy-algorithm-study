arr = [list(input()) for _ in range(5)]

length = 0
for i in range(5):
    if len(arr[i]) > length:
        length = len(arr[i])

for i in range(5):
    while len(arr[i]) < length:
        arr[i].append(-1)
arr2 = list(map(list, zip(*arr)))

result = ''
for i in range(len(arr2)):
    for j in arr2[i]:
        if j == -1:
            continue
        else:
            result += j
print(result)
