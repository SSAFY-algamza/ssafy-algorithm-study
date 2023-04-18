import sys
input = sys.stdin.readline

def check_grid():
    global sticker
    for k in range(4):
        for i in range(N):
            for j in range(M):
                if is_valid(i, j):
                    put_sticker(i, j)
                    return
        sticker = turn_sticker()
def is_valid(r, c):
    I, J = len(sticker), len(sticker[0])
    for i in range(I):
        for j in range(J):
            if sticker[i][j]:
                if r+i >= N or c+j >= M:
                    return False
                if notebook[r+i][c+j]:
                    return False
    return True

def put_sticker(r, c):
    I, J = len(sticker), len(sticker[0])
    for i in range(I):
        for j in range(J):
            if sticker[i][j]:
                notebook[r+i][c+j] = 1
def turn_sticker():
    I, J = len(sticker), len(sticker[0])
    res = []
    for j in range(J):
        temp = []
        for i in range(I-1, -1, -1):
            temp.append(sticker[i][j])
        res.append(temp)
    return res

def count_grid():
    ans = 0
    for l in notebook:
        ans += l.count(1)
    return ans

N, M, K = map(int, input().split())
notebook = [[0]*M for _ in range(N)]

for _ in range(K):
    R, C = map(int, input().split())
    sticker = [list(map(int, input().split())) for _ in range(R)]
    check_grid()

ans = count_grid()
print(ans)