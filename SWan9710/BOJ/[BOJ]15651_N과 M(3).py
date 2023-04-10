def DFS(n, lst):
    # 종료조건
    if n == M:
        print(*lst)
        return

    # 1부터 N 까지 모든 수들을 중복상관 없이 출력해 줄거
    for i in range(N):
        DFS(n + 1, lst+[arr[i]])

N, M = map(int, input().split())
arr = [i for i in range(1, N+1)]

DFS(0, [])



