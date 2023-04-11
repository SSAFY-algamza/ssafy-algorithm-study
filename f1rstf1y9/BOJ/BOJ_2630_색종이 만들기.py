def is_white(lst):
    for l in lst:
        if 1 in l:
            return False
    return True
def is_blue(lst):
    for l in lst:
        if 0 in l:
            return False
    return True
def bt(N, lst):
    global white, blue
    if is_white(lst):
        white += 1
        return
    if is_blue(lst):
        blue += 1
        return
    n = N//2
    for x, y in [(0,0), (0,n), (n, 0), (n, n)]:
        temp_lst = []
        for j in range(n):
            temp_lst.append(lst[x+j][y:y+n])
        bt(n, temp_lst)

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
white = 0
blue = 0
bt(N, paper)
print(white)
print(blue)