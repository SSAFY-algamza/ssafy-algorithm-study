'''
색종이 만들기랑 같은문제
다른점은 시작위치가 4개에서 9개로 늘어난거 뿐
그럼 재귀를 9개로 돌려주면 됨

1. 0, 0, 3
2. 0, 3, 3
3. 0, 6, 3
4. 3, 0, 3
5. 3, 3, 3
6. 3, 6, 3
7. 6, 0, 3
8. 6, 3, 3
9. 6, 6, 3

>> 일반화 시켜주기
'''

def cut(x, y, N):
    global zero, plus_one, minus_one

    for i in range(x, x+N):
        for j in range(y, y+N):
            if board[i][j] != board[x][y]:
                num = N // 3

                cut(x, y, num)                      # 0 0 3
                cut(x, y + num, num)                # 0 3 3
                cut(x, y + (num*2), num)            # 0 6 3
                cut(x + num, y, num)                # 3 0 3
                cut(x + num, y + num, num)          # 3 3 3
                cut(x + num, y + (num*2), num)      # 3 6 3
                cut(x + (num*2), y, num)            # 6 0 3
                cut(x + (num*2), y + num, num)      # 6 3 3
                cut(x + (num*2), y + (num*2), num)  # 6 6 3
                return

    # 0 갯수
    if board[x][y] == 0:
        zero += 1
    # 1 갯수
    elif board[x][y] == 1:
        plus_one += 1
    # -1 갯수
    elif board[x][y] == -1:
        minus_one += 1


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
zero = 0
plus_one = 0
minus_one = 0
#### 함수 실행 ####
cut(0,0,N)

#### 출력 순서 주의 ####
print(minus_one)
print(zero)
print(plus_one)
