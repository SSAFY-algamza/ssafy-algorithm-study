N = int(input())
for _ in range(N):
    M = int(input())
    clothes = {}
    for _ in range(M):
        name, kind = input().split()
        if kind not in clothes.keys():
            clothes[kind] = [name]
        else:
            clothes[kind].append(name)

    ans = 1
    for i in clothes.values():
        # print(i)
        ans *= len(i)+1

    print(ans-1)