import sys
readline = sys.stdin.readline
n = int(readline())
triangle = [[int(i) for i in readline().split()] for _ in range(n)]
for i in range(n-2, -1, -1):
    for j in range(i+1):
        if triangle[i+1][j] > triangle[i+1][j+1]:
            triangle[i][j] += triangle[i+1][j]
        else:
            triangle[i][j] += triangle[i+1][j+1]
print(triangle[0][0])