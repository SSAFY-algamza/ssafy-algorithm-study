'''
둘 중 작은 수를 택해서
그 수부터 거꾸로 내려가면서 둘 다 나눠보고 나눠떨어지면 그게 최대 공약수
최대공약수랑 각각 몫을 다곱하면 된다.
만약 for문을 다 통과할때까지 안나눠떨어지면 그냥 두 수의 곱이 최소공배수
'''

T = int(input())

for _ in range(T):
    A, B = map(int, input().split())
    start = min(A, B)
    ans = 0

    for i in range(start, 0, -1):  # 해당 수부터 거꾸로 해서 1까지 반복문 돌기
        a = A % i
        b = B % i
        if a == 0 and b == 0:
            ans = (A//i)*(B//i)*i
            break
    else:
        ans = A*B
    print(ans)
