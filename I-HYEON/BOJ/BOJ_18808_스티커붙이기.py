def spin(x,y):  # sticker 배열을 90도 회전시켜주는 함수
    global sticker, R, C
    temp = [[0]*x for _ in range(y)]
    for i in range(x):
        for j in range(y):
            temp[j][x-i-1] = sticker[i][j]
    sticker = temp
    R,C = C,R
    return

def check(x,y):  # 해당 좌표부터 R,C 범위 돌면서 True,False 반환해주는 함수
    # print('x,y는 여기',x,y)
    for i in range(R):
        for j in range(C):
            if 0 <= x+i < N and 0 <= y+j < M and sticker[i][j]==1 and board[x+i][y+j] == 1:  # 스티커 있는 칸에 보드에도 스티커있으면
                return False

    return True

def putting_sticker():
    # print('함수를 실행합니다')
    for i in range(N-R+1):
        for j in range(M-C+1):

            if check(i,j) == False:
                # print('이 좌표에서 붙이는건 안됨',i,j)
                continue
            else:
                # print(f'ok {i},{j}에스티커붙일수있겠다.')
                for r in range(R):
                    for c in range(C):
                        if board[i+r][j+c] == 0 and sticker[r][c] == 1:
                            board[i+r][j+c] = sticker[r][c]

                # print(f'{m + 1}번째 스티커를 붙이고 나면', board)
                return True

    return False

N, M, K = map(int, input().split())
board = [[0]*M for _ in range(N)]  # 가로길이가 M, 세로길이가 N

for m in range(K):  # 스티커 개수만큼 반복
    R, C = map(int, input().split())
    sticker = [list(map(int,input().split())) for _ in range(R)]
    # print(f'{m+1}번째 스티커 체크하는 중')

    now = 0
    flag = False
    while now != 4:

        if putting_sticker() == True:
            flag = True
            break

        spin(R,C)
        now += 1

    if flag == True:
        # print('다음으로 넘어가')
        continue

cnt = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            cnt+=1

print(cnt)