import sys
sys.stdin = open('input.txt')

def divide(x, y, N):
    global white, blue
    tmp_cnt = 0
    for i in range(x, x + N):
        for j in range(y, y + N):
            if paper[i][j]:
                tmp_cnt += 1
    if not tmp_cnt:
        white += 1
    elif tmp_cnt == N**2:
        blue += 1
    else:
        divide(x, y, N // 2)
        divide(x + N // 2, y, N // 2)
        divide(x, y + N // 2, N // 2)
        divide(x + N // 2, y + N // 2, N // 2)
    return

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
white = 0
blue = 0

divide(0, 0, N)

print(white)
print(blue)

