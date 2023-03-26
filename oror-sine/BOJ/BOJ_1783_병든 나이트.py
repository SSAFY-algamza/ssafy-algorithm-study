import sys

N, M = map(int, sys.stdin.readline().split())
moves = ((-2, 1), (-1, 2), (1, 2), (2, 1))

if (N == 1 or M == 1) or (N == 2 and M == 2):
    print(1)

elif N == 2 and M >= 3:
    moves = (M - 1) // 2
    if moves >= 4:
        moves = 3
    print(1 + moves)

elif N >= 3 and M < 7:
    moves = M - 1
    if moves >= 4:
        moves = 3
    print(1 + moves)

elif N >= 3 and M >= 7:
    print(5 + (M - 7))
