def myfunc():
    global temp_flag
    for i in range(3):
        temp = []
        for j in range(3):
            temp.append(tictacto[i][j])
        if temp.count(key) == 2:
            tictacto[i] = [key]*3
            return

    for i in range(3):
        temp = []
        for j in range(3):
            temp.append(temp_tictacto[i][j])
        if temp.count(key) == 2:
            # print('x',i)
            temp_tictacto[i] = [key]*3
            # print(temp_tictacto)
            temp_flag = True
            return

    temp_2 = []
    for i in range(3):
        temp_2.append(tictacto[i][i])
    if temp_2.count(key) == 2:
        tictacto[temp_2.index('-')][temp_2.index('-')] = key
        return

    for i,j in [(0,2),(1,1),(2,0)]:
        if tictacto[i][j] == '-':
            tictacto[i][j] = key
            return

T = int(input())

for tc in range(1, T + 1):
    tictacto = [list(input()) for _ in range(3)]
    temp_tictacto = list(zip(*tictacto))
    temp_flag = False
    key = input()

    myfunc()
    # print('?',temp_flag)
    print(f"Case {tc}:")
    if temp_flag == True:
        temp_tictacto = list(zip(*temp_tictacto))
        for t in temp_tictacto:
            print(''.join(t))
    else:
        for t in tictacto:
            print(''.join(t))