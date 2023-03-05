import sys
sys.stdin = open('input.txt')

H, W = map(int, input().split())
sky = list(input() for _ in range(H))
answer = [[0] * W for _ in range(H)]

for i in range(H):
    cloud = 0
    count = 1
    for j in range(W):
        if not cloud and sky[i][j] == '.':
            answer[i][j] = -1
        elif sky[i][j] == 'c':
            cloud = 1
            answer[i][j] = 0
            count = 1
        elif cloud == 1 and sky[i][j] == '.':
            answer[i][j] = count
            count += 1

for i in answer:
    print(*i)


