N = int(input())
input_arr = [list(map(int, input().split())) for _ in range(N)]

# 전체가 100 X 100
arr = [[0] * 102 for _ in range(102)]

for i in range(N):
    y = input_arr[i][0]
    x = input_arr[i][1]

    for iii in range(x, x+10):
        for jjj in range(y, y+10):
            arr[iii][jjj] = 1

count = 0
for i in range(102):
    for j in range(102):
        if arr[i][j] == 1:
            count += 1
print(count)