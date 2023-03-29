'''
에라스토테네스의 체 써서 거르기
2를 제외한 2의 배수 거르기
3을 제외한 3의 배수 제외
5를 제외한 5의 배수 제외
7을 제외한 7의 배수 제외
'''
N = int(input())
num = list(map(int, input().split()))
count = 0
for i in range(N):
    # 2부터 num i의 숫자까지 반복을 돌건데
    for j in range(2, num[i] + 1):
        # 소수가 되는 순간 count + 1
        if num[i] == j:
            count += 1
        # 숫자가 다를 때 j 로 나눴는데 0이다 => 소수가 아닌거
        # 더 조사할 필요 없으므로 break
        if num[i] % j == 0:
            break
print(count)