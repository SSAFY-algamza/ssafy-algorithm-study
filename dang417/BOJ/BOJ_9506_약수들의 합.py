import sys
sys.stdin = open('input.txt')

while True:
    n = int(input())
    rlt = []
    if n == -1:
        break
    for i in range(1, n):
        if not n % i:
            rlt.append(i)
    if sum(rlt) == n:
        print(f'{n} = ', end='')
        for i in range(len(rlt)-1):
            print(f'{rlt[i]} + ', end='')
        print(rlt[-1])
    else:
        print(f'{n} is NOT perfect.')