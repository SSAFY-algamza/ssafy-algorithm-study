while True:
    x, y = map(int, input().split())
    # 종료 조건
    if x == 0 and y == 0:
        break

    # 나누기 결과 검사
    # 약수인 경우
    if x < y and y % x == 0:
        print("factor")
    # 배수인 경우
    elif x > y and x % y == 0:
        print("multiple")
    # 둘다 아닌 경우
    else:
        print("neither")