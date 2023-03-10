import sys
A, B = map(int, sys.stdin.readline().split())
C = int(sys.stdin.readline())
A = (A+(B+C)//60) % 24
B = (B+C) % 60
print(A, B)
