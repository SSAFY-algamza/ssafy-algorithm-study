import sys
sys.stdin = open('input.txt')


import sys
input = sys.stdin.readline

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def diffusion(i, j):
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < R and 0 <= nj < C:
            if A[ni][nj] != (-1):
                diffused[i][j] -= A[i][j] // 5
                diffused[ni][nj] += A[i][j] // 5

def airclean():
    A[aircleaner[0]-1][0] = 0
    A[aircleaner[1]+1][0] = 0

    for i in range(aircleaner[0]-1, 0, -1):
        A[i][0] = A[i-1][0]
    for i in range(C-1):
        A[0][i] = A[0][i+1]
    for i in range(aircleaner[0]):
        A[i][C-1] = A[i+1][C-1]
    for i in range(C-1, 1, -1):
        A[aircleaner[0]][i] = A[aircleaner[0]][i-1]

    for i in range(aircleaner[1]+1, R-1):
        A[i][0] = A[i+1][0]
    for i in range(C-1):
        A[R-1][i] = A[R-1][i + 1]
    for i in range(R-1, aircleaner[1]-1, -1):
        A[i][C-1] = A[i-1][C-1]
    for i in range(C-1, 1, -1):
        A[aircleaner[1]][i] = A[aircleaner[1]][i-1]

    A[aircleaner[0]][1] = 0
    A[aircleaner[1]][1] = 0

R, C, T = map(int, input().rstrip().split())

A = [list(map(int, input().rstrip().split())) for _ in range(R)]
diffused = [A[i][::] for i in range(R)]
aircleaner = []
rlt = 0

for r in range(R):
    if A[r][0] == -1:
        aircleaner.append(r)

for _ in range(T):
    for i in range(R):
        for j in range(C):
            if A[i][j] > 0:
                diffusion(i, j)
    A = [diffused[i][::] for i in range(R)]

    airclean()

    diffused = [A[i][::] for i in range(R)]

for i in range(R):
    rlt += sum(A[i])

print(rlt + 2)



# 미세먼지는 인접한 네 방향으로 확산
# A/5 만큼 확산, 남아있는 양은 - A/5 * 확산 방향 수

# 공기청정기가 작동한다
# 위쪽은 반시계, 아래는 시계방향 순환,
# 바람이 불면 미세먼지가 바람 방향대로 모두 한칸씩 이동
