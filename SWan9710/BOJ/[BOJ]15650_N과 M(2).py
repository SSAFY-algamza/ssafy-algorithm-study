def DFS(num, lst):
    # 종료조건
    if num > N:
        if len(lst) == M:
            result.append(lst)
        return

    # 숫자를 선택한 경우
    DFS(num + 1, lst + [num])

    # 숫자를 선택 안한 경우
    DFS(num + 1, lst)

N, M = map(int, input().split())
result = []
DFS(1, [])
for i in result:
    print(*i)


