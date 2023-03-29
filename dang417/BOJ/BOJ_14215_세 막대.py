import sys
sys.stdin = open('input.txt')

tri_lst = sorted(list(map(int, input().split())))
while True:
    if tri_lst[-1] < tri_lst[0] + tri_lst[1]:
        print(sum(tri_lst))
        break
    else:
        tri_lst[-1] -= 1