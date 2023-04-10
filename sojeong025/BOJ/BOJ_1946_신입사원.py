import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    rank = [list(map(int, input().split())) for _ in range(N)]

    rank_high = sorted(rank)

    person = rank_high[0][1]
    cnt = 1
    top = 0
    for i in range(1, len(rank_high)):
        if rank_high[i][1] < rank_high[top][1]:
            top = i
            cnt += 1

    print(cnt)

