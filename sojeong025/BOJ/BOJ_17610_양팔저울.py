import sys
sys.stdin = open('input.txt')

def DFS(L, sum):
    global res
    if L == k:
        if 0 < sum <= s:
            res.add(sum)

    else:
        DFS(L+1, sum + gram[L])
        DFS(L+1, sum - gram[L])
        DFS(L+1, sum)


k = int(input())
gram = list(map(int, input().split()))

s = sum(gram)
res = set()
DFS(0,0)
print(s-len(res))
