while True:
    a = int(input())

    if a == -1:
        break

    lst = []
    for i in range(a-1,0,-1):
        if not a % i :
            lst.append(i)

    lst.sort()

    if sum(lst) == a:
        print(f"{a} = "+" + ".join(str(i) for i in lst))
    else:
        print(f'{a} is NOT perfect.')