import sys
sys.stdin = open('input.txt')

N = int(input())
paper = [[0] * 101 for _ in range(101)]

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

for _ in range(N):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            paper[i][j] = 1

length = 0
for x in range(101):
    for y in range(101):
        if paper[x][y] ==1:
            count = 0
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if paper[nx][ny] == 1:
                    count += 1
            if count == 4:
                continue
            elif count == 3:
                length += 1
            elif count == 2:
                length +=2
print(length)


