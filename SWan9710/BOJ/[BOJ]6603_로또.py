def DFS(n, s, lst):
    if n == 6:
        result.append(lst)
        return

    for j in range(s, N):
        DFS(n+1, j+1, lst+[arr[j]])

while True:
    input_lst = list(map(int, input().split()))
    if input_lst[0] == 0:
        break

    N = input_lst[0]
    arr = input_lst[1:]
    result = []

    DFS(0,0,[])

    for i in result:
        print(*i)
    print()