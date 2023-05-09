def recur(alpha, pre, cnt):
    global ans
    if cnt >= ans:
        return
    if alpha == 26:
        ans = cnt
        return

    if low[alpha] == -1:
        recur(alpha+1, pre, cnt)
    elif low[alpha] == high[alpha]:
        recur(alpha+1, low[alpha], cnt + abs(pre-low[alpha]))
    else:
        recur(alpha+1, low[alpha], cnt + abs(pre-high[alpha]) + high[alpha]-low[alpha])
        recur(alpha+1, high[alpha], cnt + abs(pre-low[alpha]) + high[alpha]-low[alpha])

S = input()
low = [-1]*26
high = [-1]*26
ans = 1e9

for i in range(len(S)):
    alpha = ord(S[i])-97
    if low[alpha] == -1:
        low[alpha] = i
    high[alpha] = i

recur(0, 0, 0)
print(ans+len(S))
