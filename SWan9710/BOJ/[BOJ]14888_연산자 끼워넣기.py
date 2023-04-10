def check(value, depth, plus, minus, mul, div):
    global max_v, min_v
    # 종료조건
    if N == depth:
        max_v = max(max_v, value)
        min_v = min(min_v, value)
        return

    if plus:
        check(value + num[depth], depth + 1, plus - 1, minus, mul, div)
    if minus:
        check(value - num[depth], depth + 1, plus, minus - 1, mul, div)
    if mul:
        check(value * num[depth], depth + 1, plus, minus, mul - 1, div)
    if div:
        check(int(value / num[depth]), depth + 1, plus, minus, mul, div - 1)


# 숫자의 갯수
N = int(input())
num = list(map(int, input().split()))
# 연산자
plus, minus, mul, div = map(int, input().split())

# 값을 비교하며 최대 최소를 바꿔주기 위해 음수와 양수를 반대로 할당
max_v = int(-1e10)
min_v = int(1e10)

# 출력은? 최대값과 최소값 각각 출력해주기
check(num[0], 1, plus, minus, mul, div)
print(max_v)
print(min_v)



