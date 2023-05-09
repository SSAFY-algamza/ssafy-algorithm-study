'''
크기가 r*c인 격자판이 있음
격자의 각 칸은 비어있거나(.로 표시) 폭탄이 들어있음(o로 표시)
폭탄이 있는 칸은 3초가 지난 후 폭발하는데, 폭발을 하면 본인포함 상하좌우 네 칸도 함께 폭발한다.
폭발의 결과는 빈칸(.로표시)이 되는 것.

(1초 후)초기상태가 있고
(2초 후)봄버맨이 폭탄이 없는 곳에 모두 폭탄을 설치한다
(3초 후 / 1초 후)먼저 설치된 폭탄이 터진다

여기서 부터 반복
(2초 후)봄버맨이 폭탄이 없는 곳에 모두 폭탄을 설치한다
(3초 후) 먼저 설치된 폭탄이 터진다

r,c,n(n은 주어진 시간)이 주어질때 n초 후 격자판 상태를 출력할 것

아이디어>>
1. 격자판을 읽어온다.
2. 격자판을 두번 순회한다.
2-1. 첫번째 순회때, 이미 설치된 폭탄의 좌표를 읽어온다. 돌면서 해당 좌표가 비어있으면 설치하고, 이미 있으면 좌표에 추가한다.
2-2. 두번째 순회때, 리스트에 있는 폭탄의 좌표를 이용해 인접영역 5개를 폭파시킨다.(.으로 바꾼다.)
2번 과정을 while문 안에 넣고 시간이 n초가 될때까지 반복한다.
'''


r, c, n = map(int,input().split())
grid = []
for _ in range(r):
    grid.append(list(input()))

time = 1
while time < n:
    bombs = []
    for i in range(r):
        for j in range(c):
            if grid[i][j] == '.':
                grid[i][j] = 'O'
            else:
                bombs.append((i,j))
    else:
        time += 1

    if time == n:
        break

    for i,j in bombs:
        grid[i][j] = '.'
        for k in [(1,0),(-1,0),(0,1),(0,-1)]:
            ni = i + k[0]
            nj = j + k[1]
            if ni<0 or ni>= r or nj<0 or nj >=c: continue
            grid[ni][nj] = '.'
    else:
        time += 1

for i in range(r):
    print(''.join(grid[i]))
