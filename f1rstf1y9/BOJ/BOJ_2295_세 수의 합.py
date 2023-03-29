N = int(input())
U = []
for _ in range(N):
    U.append(int(input()))

dict = {}
for i in range(N):
    for j in range(N):
        dict[U[i]+U[j]] = dict.get(U[i]+U[j], 0) + 1

ans = 0
for i in range(N):
    for j in range(N):
        if dict.get(U[i]-U[j]):
            ans = max(ans, U[i])
print(ans)