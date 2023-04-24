A = int(input())
T = int(input())
bundegi = int(input())
lst = []

bun_cnt = degi_cnt = 1
cycle = 0

while True:
    before_num = bun_cnt
    cycle += 1
    for _ in range(2):
        lst.append((bun_cnt,0))
        bun_cnt += 1
        lst.append((degi_cnt,1))
        degi_cnt += 1
    for _ in range(cycle+1):
        lst.append((bun_cnt,0))
        bun_cnt += 1
    for _ in range(cycle+1):
        lst.append((degi_cnt,1))
        degi_cnt += 1

    if before_num < T < bun_cnt:
        print(lst.index((T,bundegi))%A)
        break