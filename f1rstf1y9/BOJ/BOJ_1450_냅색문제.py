def count_case(n):
    s = 0
    e = len(A_case)-1
    while s < e:
        m = s+(e-s)//2
        if A_case[m]+n <= C:
            s = m+1
        else:
            e = m
    if A_case[s]+n <= C:
        return s+1
    else:
        return s

N, C = map(int,input().split())
w = list(map(int, input().split()))

A_case = [0]
B_case = [0]
for i in range(N):
    temp = []
    if i < N//2:
        for j in A_case:
            temp.append(j+w[i])
        A_case.extend(temp)
    else:
        for j in B_case:
            temp.append(j + w[i])
        B_case.extend(temp)
A_case.sort()

cnt = 0
for i in B_case:
    cnt += count_case(i)
print(cnt)