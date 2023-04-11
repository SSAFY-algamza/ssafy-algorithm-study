def bt(idx, p, f, s, v, cost, cur_list):
    global min_cost, min_list
    if p >= mp and f >= mf and s >= ms and v >= mv and min_cost >= cost:
        if min_cost == cost:
            min_list.append(cur_list)
        else:
            min_list = [cur_list]
        min_cost = cost
        return

    if min_cost <= cost or idx >= N:
        return

    cur = ingred[idx+1]
    bt(idx+1, p+cur[0], f+cur[1], s+cur[2], v+cur[3], cost+cur[4], cur_list+[idx+1])
    bt(idx+1, p, f, s, v, cost, cur_list)

N = int(input())
mp, mf, ms, mv = map(int, input().split())
#단백질, 지방, 탄수화물, 비타민, 가격
ingred = [0]+[list(map(int, input().split())) for _ in range(N)]

min_cost = 500*N
min_list = []
for i in range(1, N+1):
    ing_list = [i]
    bt(i, *ingred[i], ing_list)
if min_list:
    print(min_cost)
    print(*sorted(min_list)[0])
else:
    print(-1)