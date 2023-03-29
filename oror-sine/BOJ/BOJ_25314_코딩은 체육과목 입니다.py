import sys

N = int(sys.stdin.readline())
ans = (N // 4) + (1 if N % 4 else 0)
print("long " * ans + "int")
