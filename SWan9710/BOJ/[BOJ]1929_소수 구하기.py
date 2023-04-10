'''
M 이상 N 이하의 소숙가 하나 이상 있는 입력만 주어진다
한 줄에 하나씩 증가하는 순서대로 소수를 출력
소수 구할때 2, 3, 5, 7 은 무조건 그냥 출력
'''
M, N = map(int, input().split())
# for i in range(M, N+1):
#     div = 2
#     while True:
#         # 종료조건
#         if i == div:
#             print(i)
#             break
#         if i % div == 0:
#             break
#         else:
#             div += 1

# i의 제곱근을 구해서 +1 해주면 해당 수의 제곱근이 나온다.
# 전체를 검사하면 M, N의 범위가 커지면 계산량이 많아져서 시간초과 뜸
# 에라토스테네스의 체가 2, 3, 5, 7 의 배수에 해당하는 모든 수는 무조건 소수가 아님
# 해당 수들을 제외한 나머지 수가 소수
for i in range(M, N+1):
    if i == 1:
        continue
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            break
    else:
        print(i)
