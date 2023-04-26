import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

def move_up(original_board):
    board = [0] * N
    for i in range(N):
        board[i] = original_board[i][::]
    for j in range(N):
        for i in range(N):
            if board[i][j]:
                for k in range(i+1, N):
                    if board[i][j] == board[k][j]:
                        board[i][j] *= 2
                        board[k][j] = 0
                        break
                    elif board[k][j]:
                        break
    for _ in range(N):
        for j in range(N):
            for i in range(N-1):
                if not board[i][j]:
                    board[i][j], board[i+1][j] = board[i+1][j], board[i][j]

    return board
def move_down(original_board):
    board = [0] * N
    for i in range(N):
        board[i] = original_board[i][::]
    for j in range(N):
        for i in range(N-1, -1, -1):
            if board[i][j]:
                for k in range(i-1, -1, -1):
                    if board[i][j] == board[k][j]:
                        board[i][j] *= 2
                        board[k][j] = 0
                        break
                    elif board[k][j]:
                        break
    for _ in range(N):
        for j in range(N):
            for i in range(N-1, 0, -1):
                if not board[i][j]:
                    board[i][j], board[i-1][j] = board[i-1][j], board[i][j]

    return board
def move_left(original_board):
    board = [0] * N
    for i in range(N):
        board[i] = original_board[i][::]
    for i in range(N):
        for j in range(N):
            if board[i][j]:
                for k in range(j+1, N):
                    if board[i][j] == board[i][k]:
                        board[i][j] *= 2
                        board[i][k] = 0
                        break
                    elif board[i][k]:
                        break
    for _ in range(N):
        for i in range(N):
            for j in range(N-1):
                if not board[i][j]:
                    board[i][j], board[i][j+1] = board[i][j+1], board[i][j]

    return board
def move_right(original_board):
    board = [0] * N
    for i in range(N):
        board[i] = original_board[i][::]
    for i in range(N):
        for j in range(N-1, -1, -1):
            if board[i][j]:
                for k in range(j-1, -1, -1):
                    if board[i][j] == board[i][k]:
                        board[i][j] *= 2
                        board[i][k] = 0
                        break
                    elif board[i][k]:
                        break
    for _ in range(N):
        for i in range(N):
            for j in range(N-1, 0, -1):
                if not board[i][j]:
                    board[i][j], board[i][j-1] = board[i][j-1], board[i][j]

    return board

def DFS(board, cnt):
    global rlt

    maxv = 0
    for i in range(N):
        for j in range(N):
            if maxv <= board[i][j]:
                maxv = board[i][j]

    if rlt <= maxv:
        rlt = maxv

    if cnt == 5:
        return

    board_up = move_up(board)
    DFS(board_up, cnt+1)

    board_down = move_down(board)
    DFS(board_down, cnt+1)

    board_left = move_left(board)
    DFS(board_left, cnt+1)

    board_right = move_right(board)
    DFS(board_right, cnt+1)

    return

N = int(input())
first_board = [list(map(int, input().rstrip().split())) for _ in range(N)]
rlt = 0

DFS(first_board, 0)

print(rlt)