import sys
N = int(sys.stdin.readline())
paper = [[int(i) for i in sys.stdin.readline().split()] for _ in range(N)]
ds = ((1, 0), (0, 1))
def sol(paper, r, c, l):
    ans = [0, 0]
    if l == 1:
        ans[paper[r][c]] += 1
        return ans
    l //= 2
    for white, blue in sol(paper, r, c, l), sol(paper, r+l, c, l), sol(paper, r, c+l, l), sol(paper, r+l, c+l, l):
        ans[0] += white
        ans[1] += blue
    if ans[0] == 0:
        return [0, 1]
    if ans[1] == 0:
        return [1, 0]
    return ans

w, b = sol(paper, 0, 0, N)
print(w)
print(b)
