import sys
sys.stdin = open('input.txt', 'r')

def backtracking(n):
    global cnt
    if n == N:
        cnt += 1
        return
    
    for j in range(N):
        if board1[j] == board2[n+j] == board3[n-j]==0:
            board1[j] = board2[n+j] = board3[n-j] = 1
            backtracking(n+1)
            board1[j] = board2[n+j] = board3[n-j] = 0
            

N = int(input())
cnt = 0
board1 = [0] * N
board2 = [0] * (2*N)
board3 = [0] * (2*N)
backtracking(0)
print(cnt)


