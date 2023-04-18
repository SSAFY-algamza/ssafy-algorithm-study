N = int(input())  # 체스판의 가로 칸수이자 세로 칸수
chass = [0] * N
cnt = 0

def is_promising(x):  # x에 들어오는 값이 현재 행의 번호, chass[x]가 현재 열의 번호
    for i in range(x):
        if chass[i] == chass[x] or abs(i-x) == abs(chass[i]-chass[x]):  # 조건 중 하나면
            return False
    return True

def backtrack(row):  # 행을 깊이 삼아 깊이 우선 탐색 + 백트랙킹
    global cnt
    if row == N:  # 깊이가 끝까지 다다랐을 때
        cnt += 1  # 경우의 수 하나를 올려주고
        return  # 함수를 끝낸다

    for i in range(N):
        chass[row] = i  # 해당 깊이에서 열 하나를 고른 다음 재귀호출로 dfs를 할건데
        if is_promising(row):  # 지금 단계가 유망한 경우만 재귀 호출할 것임
            backtrack(row+1)


backtrack(0)
print(cnt)