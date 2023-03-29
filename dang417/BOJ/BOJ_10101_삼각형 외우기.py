import sys
sys.stdin = open('input.txt')

theta_lst = list(int(input()) for _ in range(3))

if theta_lst[0] == theta_lst[1] == theta_lst[2] == 60:
    print('Equilateral')
elif sum(theta_lst) == 180:
    if theta_lst[0] == theta_lst[1] or theta_lst[1] == theta_lst[2] or theta_lst[0] == theta_lst[2]:
        print('Isosceles')
    else:
        print('Scalene')
else:
    print('Error')