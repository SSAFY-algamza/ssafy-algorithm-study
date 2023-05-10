# 제곱ㄴㄴ수 : 1보다 큰 제곱수로 나누어 떨어지지 않는 수
# 제곱ㅇㅇ수 : 1보다 큰 제곱수로 나누어 떨어지는 수

# 1 ≤ min ≤ 1,000,000,000,000
# min ≤ max ≤ min + 1,000,000

# [issue] 정수 오버플로우 (JAVA, C/C++)
# 1,000,000,000,000 이정도 수는 32bit로 표현할 수 없음
# python : 파이썬의 int는 오버플로우가 없음
# javascript : 기본적으로 64bit double
# [sol]
# JAVA : long, C/C++ : long long 

# [issue] 메모리 초과
# 1,000,000,000,000 이정도 길이의 리스트는 메모리 초과
# [sol]
# 1,000,000 이정도는 괜찮기 때문에, min 부터 max 까지만 저장 

# [issue] 시간 초과
# [sol] 
# 1. 제수(divisor)가 제곱수이므로, for문은 2부터 MAX의 제곱근(SQRT_MAX)까지
# 2. 구간 [2, SQRT_MAX]의 수 중 소수인 수
#     제곱ㄴㄴ수 판별 시, `소수의 제곱`의 배수인지만 판별하면 된다.
#     ex) 16(4)의 배수는 모두 4(2)의 배수, 중복제거
# 3. for문 시, range의 step 활용

MIN, MAX = map(int, input().split())
SQRT_MAX = int(MAX**(1/2))
isNONO = [True for _ in range(MIN, MAX+1)]
isPrime = [True]*(SQRT_MAX+1)

for i in range(2, SQRT_MAX+1):
    if isPrime[i] == False: continue
    for j in range(i+i, SQRT_MAX+1, i): # 소수 자신을 제외한, 자신의 배수 
        isPrime[j] = False 

for i in range(2, SQRT_MAX+1):
    if not isPrime[i]: continue  # 소수가 아니면 continue
    step = i*i  # 소수의 제곱수
    start = step
    if MIN%step: start *= (MIN//step+1)
    else: start *= (MIN//step)  # start: 구간 [min, max]의 가장 작은 제곱ㅇㅇ수
    for j in range(start, MAX+1, step):  # 구간 [start, MAX] 중, 제곱수의 배수
        isNONO[j-MIN] = False 

print(sum(isNONO))  # True 값의 수 == 제곱ㄴㄴ의 수
