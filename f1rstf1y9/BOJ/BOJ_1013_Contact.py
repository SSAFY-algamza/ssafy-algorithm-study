import re

T = int(input())
for _ in range(T):
    string = input()
    r = re.compile('(100+1+|01)+')
    isMatch = r.fullmatch(string)
    if isMatch:
        print("YES")
    else:
        print("NO")
