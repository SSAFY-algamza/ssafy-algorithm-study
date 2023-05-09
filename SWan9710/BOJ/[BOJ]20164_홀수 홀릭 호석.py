'''
1. 입력받는 수들의 홀수 갯수 세주기
2. 수가 한자리 이상인지 판별 후 한자리이면 종료
3. 두자리인 경우 그 숫자들 더해서 새로운 수로 만들고 그 수 다시 홀수인지 갯수 세주기
4. 3자리 이상인 경우 반복문으로 자리 쪼개서 재귀로 자리별로 홀수 갯수 세서 결과에 저장

결과에서 최솟값과 최댓값 출력하기
'''

# 홀수 갯수 세주기
def CountOddNumber(num):
    oddnumber = 0
    while num:
        # 나머지가 1 이상인 홀수인 경우
        if (num % 10) % 2:
            oddnumber += 1
        num //= 10
    return oddnumber

# 수의 자릿수 판별
def digit(num, total_odd_count):
    # 종료조건
    if len(num) == 1:
        # 지금까지 나온 홀수의 갯수를 결과배열에 저장 후 종료
        result.append(total_odd_count)
        return
    
    # 2자릿수 인 경우
    elif len(num) == 2:
        # 문자열 형태이니 각 자릿수를 쪼개서 int로 묶어서 새로운수로 만들기
        new_num = int(num[0]) + int(num[1])
        # 지금까지 나온 홀수의 갯수에 현재수의 홀수갯수 세서 더해서 재귀실행
        # 그때의 결과값이 result에 쌓이게 된다.
        digit(str(new_num), total_odd_count + CountOddNumber(new_num))

    # 3자리 이상안 경우
    for i in range(1, len(num)):
        for j in range(i+1, len(num)):
            start = num[:i]
            mid = num[i:j]
            end = num[j:]
            new_num = int(start) + int(mid) + int(end)
            digit(str(new_num), total_odd_count + CountOddNumber(new_num))

# 입력받는 수를 문자로 입력받아서 자릿수 세주는 걸 편하게 해주기
# 숫자로 입력받으면 숫자를 10으로 나눈 몫이랑 나머지로 더해주는 복잡한 걸 해야하는데 걍 문자로 입력받아서 자리별로 쪼개서 그걸 int로 묶어서 더해버리면 더 편함
N = input()
result = []
digit(N, CountOddNumber(int(N)))
print(result)
print(min(result), max(result))