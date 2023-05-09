from itertools import combinations
N = input()

def count_odd(num):
    cnt = 0
    for n in num:
        cnt += 1 if int(n)%2 else 0
    return cnt

def calc(n, cnt):
    global min_v, max_v
    if len(n) == 1:
        min_v = min(min_v, cnt)
        max_v = max(max_v, cnt)
        return
    if len(n) == 2:
        new_n = str(int(n[0])+int(n[1]))
        c = 0
        for n in new_n:
            c += 1 if int(n) % 2 else 0
        calc(new_n, cnt + c)
    else:
        for i, j in combinations(range(1,len(n)),2):
            new_n = str(int(''.join(n[:i])) + int(''.join(n[i:j])) + int(''.join(n[j:])))
            c = 0
            for k in new_n:
                c += 1 if int(k) % 2 else 0
            calc(new_n, cnt + c)
min_v = 1e9
max_v = 0
cnt = 0
for n in N:
    cnt += 1 if int(n)%2 else 0
calc(N, cnt)
print(min_v, max_v)
