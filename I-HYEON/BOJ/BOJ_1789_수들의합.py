N = int(input())

cnt = 0
next_num = 1
remain_num = N

while remain_num >= next_num:
    remain_num -= next_num

    next_num += 1
    cnt += 1

print(cnt)