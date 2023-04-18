N = int(input())  # 가로길이 입력
DP = [0] * 31  # N +1 크기로 초기화한 DP 배열

DP[2] = 3  # 가로 길이 2일때 경우의 수는 3

for i in range(4, N+1, 2):  # 가로가 홀수일 때는 의미 없으므로 건너뜀
    DP[i] = DP[i-2] * 3 + 2

    for j in range(4, i, 2):  # 매번 생기는 특수한 경우의 수 2가지 처리
        DP[i] += DP[i-j] * 2    # 벽의 가로 길이가 i-j 일때의 경우의 수와 곱한 값을 dp에 추가

print(DP[N])