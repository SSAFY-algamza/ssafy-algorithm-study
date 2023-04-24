'''
n줄에 걸쳐 지뢰판 정보를 읽어온다.(land_mines 에 할당)
n줄에 걸쳐 확인한 곳/확인안한 곳 정보를 읽어온다(is_checked 에 할당)

이중 for문을 통해 매 좌표에 접근한다음
만약, is_checked 보드에 x(이미확인한곳) 문자가 있다면 land_mides 해당 위치가 지뢰가 아닌걸 확인후 , land_mines 배열 8방향 탐색으로 지뢰를 읽어와 넣고
                      .(아직안열어본 곳) 문자가 있다면 그냥 그대로 점을 읽어와 넣는다.
다만, land_mines 해당 위치가 지뢰로 확인이 되면, find 플래그를 True로 표시해둔다. 그리고 제일 마지막에 find가 True라면 모든 지뢰를 표시해준다.
'''

N = int(input())
land_mine = [input() for _ in range(N)]
is_checked = [input() for _ in range(N)]
answer = [['']*N for _ in range(N)]
find = False
for i in range(N):
    for j in range(N):

        if is_checked[i][j] == '.':
            if answer[i][j] == '*':
                continue
            else:
                answer[i][j] = '.'
        elif is_checked[i][j] == 'x':
            if land_mine[i][j] == '.':
                mine_cnt = 0
                for di,dj in [(1,0),(-1,0),(0,1),(0,-1),(-1,-1),(-1,1),(1,-1),(1,1)]:
                    ni = i + di
                    nj = j + dj
                    if 0 <= ni < N and 0 <= nj < N and land_mine[ni][nj] == '*':
                        mine_cnt += 1
                answer[i][j] = str(mine_cnt)
            elif land_mine[i][j] == '*':
                find = True

if find == True:
    for x in range(N):
        for y in range(N):
            if land_mine[x][y] == '*':
                answer[x][y] = '*'

for a in range(N):
    print(''.join(answer[a]))