import sys
sys.stdin = open('input.txt')

K = int(input())
width = []
height = []
length = []

for _ in range(6):
    # 1 동쪽 2 서쪽 3 남쪽 4 북쪽
    dir, dis = map(int, input().split())
    if dir == 1 or dir == 2:
        width.append(dis)
        length.append(dis)
    elif dir == 3 or dir == 4:
        height.append(dis)
        length.append(dis)

max_square = max(width) * max(height)

max_width = length.index(max(width))
max_height = length.index(max(height))

# print(length)
# print(max_width, max_height)

empty_width = abs(length[(max_height + 1) % 6] - length[(max_height - 1) % 6])
empth_height = abs(length[(max_width + 1) % 6] - length[(max_width - 1) % 6])

empth_square = empth_height * empty_width
print(K * (max_square - empth_square))
