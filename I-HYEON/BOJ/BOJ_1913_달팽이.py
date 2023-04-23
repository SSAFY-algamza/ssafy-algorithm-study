'''
시작 숫자는 N*N/ 시작 좌표는 (0,0)지점부터 거꾸로 돌면서
벽에 부딪히거나 이미 숫자가 적힌 경우 델타 방향을 전환하면서
숫자를 채울 예정
'''

N = int(input())
key = int(input())
delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]
lst = [[0]*N for _ in range(N)]

now = (0, 0)  # 시작 포인트
num = N*N  # 시작 숫자
direction = 0  # 델타 시작점
key_i, key_j = 0, 0

while num != 0:

    x, y = now  # 좌표 하나씩 할당

    if num == key:  # 찾고 있는 숫자라면 값 저장해주고
        key_i = x
        key_j = y
    lst[x][y] = num  # 해당 자리에 숫자를 집어넣는다.

    nx = x + delta[direction][0]
    ny = y + delta[direction][1]
    if nx < 0 or nx >= N or ny < 0 or ny >= N or lst[nx][ny] != 0 :  # 새 좌표가 배열을 벗어났다면
        nx, ny = x, y  # 되돌려놓고
        direction = (direction+1) % 4  # 델타 방향을 바꿔 준 후 재시도
        nx = x + delta[direction][0]
        ny = y + delta[direction][1]

    now = (nx, ny)  # 다음 now 좌표에 넣어준다
    num -= 1  # 숫자도 하나 올려준다

for i in range(N):
    print(' '.join(list(map(str,lst[i]))))
print(key_i+1, key_j+1)