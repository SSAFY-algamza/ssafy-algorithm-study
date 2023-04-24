def bingo_check():  # 빙고 줄 검사
    ans = 0
    reverse_board = list(map(list,zip(*board)))  # 세로 검사에 사용할 전치 행렬

    row = 0  # 가로 개수 카운트
    for i in range(5):
        if board[i].count(0) == 5:
            row += 1

    col = 0  # 세로 개수 카운트
    for i in range(5):
        if reverse_board[i].count(0) == 5:
            col += 1

    right = 0
    left = 0
    right_cnt = 0
    left_cnt = 0
    for di, dj in zip(range(5),range(5)):
            if board[di][dj] == 0:  # 카운트
                right_cnt += 1
            if board[di][4-dj] == 0:  # 마찬가지
                left_cnt += 1
    if right_cnt == 5:
        right = 1
    if left_cnt == 5:
        left = 1

    ans = row+col+right+left
    return ans

board = []
for _ in range(5):
   board.append(list(map(int, input().split())))  # 빙고판 받아오기

mc_says = []
for _ in range(5):
    mc_says.extend(list(map(int, input().split())))  # mc가 말하는 숫자 받아오기

ans = 0

for m in range(25):  # mc가 말하는 숫자에 인덱스로 접근

    flag = True
    for i in range(5):
        for j in range(5):  # 숫자를 고정시키고, 배열을 순회해서 그 숫자가 있는 곳을 찾아냄
            if board[i][j] == mc_says[m]:  # 사회자가 부른 숫자를
                board[i][j] = 0  # 보드판에서 0으로 변경
                if bingo_check() >= 3:  # 빙고판의 빙고줄을 세는 함수가 3보다 크거나 같으면
                    ans = m + 1  # 그때 숫자를 답에 할당
                flag = False
                break

        if flag == False:
            break
    if ans:
        break

print(ans)