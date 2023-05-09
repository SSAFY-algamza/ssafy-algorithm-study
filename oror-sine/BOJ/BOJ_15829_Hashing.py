dic = {chr(ord('a')+i): i+1 for i in range(26)}
input()
H = 0
r = 1
rr = 31
M = 1234567891
for c in input():
    H += dic[c] * r
    H %= M
    r *= rr
print(H)
