def dfs(num, money):
    global answer, visited
    if answer == 1:
        return
    if rooms[num][0] == 'L':  # 레프리콘
        if rooms[num][1] > money:
            money = rooms[num][1]
    elif rooms[num][0] == 'T':  # 트롤
        if rooms[num][1] > money:
            return
        else:
            money -= rooms[num][1]
            
    if num == n - 1:
        answer = 1
        return

    visited[num] = True
    for i in rooms[num][2]:
        if visited[int(i) - 1] == False:
            dfs(int(i) - 1,money)
    visited[num] = False


while True:
    n = int(input())
    if n == 0: break

    visited = [False] * n
    money = 0
    rooms = []
    answer = 0

    for _ in range(n):
        tmp = input().split()
        rooms.append([tmp[0], int(tmp[1]), tmp[2:-1]])

    dfs(0, 0)

    if answer == 0:
        print('No')
    else:
        print('Yes')
