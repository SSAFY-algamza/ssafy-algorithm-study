def recursion(s, l, r):
    global count
    count += 1
    if l >= r: return 1, count
    elif s[l] != s[r]: return 0, count
    else: return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

N = int(input())
for i in range(N):
    count = 0
    arr = input()
    print(*isPalindrome(arr))
