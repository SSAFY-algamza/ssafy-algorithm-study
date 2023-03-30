import sys
sys.stdin = open('input.txt')

def backtracking(i, tmp):
    global cnt

    if i == N:
        cnt += 1
        return
    
    for j in range(N):
        # 현재 근육량 + 현재 운동 키트 중량 - K가 0 이상일때만 재귀
        if visited[j] or tmp + kit[j] - K < 0:
            continue
        visited[j] = 1
        backtracking(i+1, tmp + kit[j] - K)
        visited[j] = 0


N, K = map(int, input().split())
kit = list(map(int, input().split()))

visited = [0] * N
cnt = 0

backtracking(0, 0)
print(cnt)