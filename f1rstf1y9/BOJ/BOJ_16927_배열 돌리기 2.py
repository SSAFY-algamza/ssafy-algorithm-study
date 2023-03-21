N, M, R = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

tmp = []
for i in range(min(N,M)//2):
    tmp.append(2*((N-2*i) + (M-(2*i)))-4)

for i in range(min(N,M)//2):
    for j in range(R%tmp[i]):
        t = A[i][i]
        for k in range(1+i, M-i):
            A[i][k-1] = A[i][k]
        for k in range(1+i, N-i):
            A[k-1][M-1-i] = A[k][M-1-i]
        for k in range(1+i, M-i):
            A[N-1-i][M-k] = A[N-1-i][M-1-k]
        for k in range(1+i, N-i):
            A[N-k][i] = A[N-1-k][i]

        A[1+i][i] = t

for n in A:
    print(*n, sep=' ')
