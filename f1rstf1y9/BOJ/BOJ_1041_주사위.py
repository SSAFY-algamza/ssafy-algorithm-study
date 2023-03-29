three = [(0,1,2),(0,1,3),(0,2,4),(0,3,4),(1,2,5),(1,3,5),(2,4,5),(3,4,5)]
N = int(input())
dice = list(map(int, input().split()))
if N != 1:
    three_min = two_min = 1e7
    for a,b,c in three:
        three_ = dice[a]+dice[b]+dice[c]
        two_ = min(dice[a]+dice[b], dice[b]+dice[c], dice[a]+dice[c])
        if three_ < three_min:
            three_min = three_
        if two_ < two_min:
            two_min = two_
    one_min = min(dice)
    total = 4*three_min
    total += (8*N-12)*two_min
    total += (5*N**2-16*N+12)*one_min
else:
    total = sum(dice)-max(dice)
print(total)
