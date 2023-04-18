def find_n(exc, n):
    s, e = 0, N-1
    while s < e:
        sum_v = A[s]+A[e]
        if sum_v < n:
            s += 1
        elif sum_v > n:
            e -= 1
        else:
            if s == exc:
                s += 1
            elif e == exc:
                e -= 1
            else:
                return 1
    return 0


N = int(input())
A = list(map(int, input().split()))
A.sort()
ans = 0
for i in range(N):
    ans += find_n(i, A[i])
print(ans)
