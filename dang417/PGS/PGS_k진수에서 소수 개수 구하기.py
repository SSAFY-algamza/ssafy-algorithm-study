import math

def solution(n, k):

    def check_prime(num):
        if num.isdigit() and not num == '1':
            num = int(num)
            for i in range(2, int(math.sqrt(num))+1):
                if not num % i:
                    return 0
            return 1
        else:
            return 0

    def change_knum(n, k):
        rlt = ''
        while True:
            if n == 0:
                return rlt
            rlt += str(n % k)
            n = n//k

    num_arr = change_knum(n, k)[::-1]
    num_arr = ''.join(num_arr).split('0')
    answer = 0

    for num in num_arr:
        answer += check_prime(num)

    return answer

n = 437674
k = 3
print(solution(n, k))
