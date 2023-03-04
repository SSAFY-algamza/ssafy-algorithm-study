import sys
sys.stdin = open('input.txt')

bingo1 = [list(map(int, input().split())) for _ in range(5)]
bingo2 = list(map(list, zip(*bingo1)))

bingo3 = []
bingo4 = []
for i in range(len(bingo1)):
    bingo3.append(bingo1[i][i])
    bingo4.append(bingo1[4-i][i])

# 빙고가 될 모든 경우의 수 완성 [[][][][]] 12개 경우의
bingo = bingo1 + bingo2
bingo.append(bingo3)
bingo.append(bingo4)


number = [list(map(int, input().split())) for _ in range(5)]
number = sum(number, [])

answer = 0
for i in number:
    cnt = 0
    answer += 1
    for j in bingo:
        if i in j:
            j.remove(i)
        if j == []:
            cnt += 1
    if cnt >= 3:
        break
print(answer)
