'''
인덱스마다
증가하는 가장 긴 부분 수열을 구하고
감소하는 가장 긴 부분 수열을 구해서(이 때는 거꾸로 접근)
그 둘의 합이 가장 클 때 가장 긴 바이토닉 수열이 된다.
k값이 중복되므로 마지막에 1빼주는 것 잊지않기
'''

N = int(input())
lst = list(map(int, input().split()))
reverse_lst = lst[::-1]

dp1 = [1 for _ in range(N)]  # 증가하는 부분 수열 구할 때 쓰는 DP 배열
dp2 = [1 for _ in range(N)]  # 감소하는 부분 수열 구할 때 쓰는 DP 배열

for i in range(N):  # 모든 인덱스에 접근하는데, 접근할때마다
    for j in range(i):  # 해당 인덱스까지만 반복해서 j를 가져온다
        if lst[j] < lst[i]:  # 증가하는 부분 수열이라는 조건에 맞아들면
            dp1[i] = max(dp1[i],dp1[j]+1)  # j 인덱스까지의 완성된 부분 수열에 1을 더한 값으로 완성, 최대값 갱신
        if reverse_lst[j] < reverse_lst[i]:  # 거꾸로 만든 리스트로도 같은 행동을 반복하면
            dp2[i] = max(dp2[i],dp2[j]+1)  # 나중에 다시 뒤집었을 때 감소하는 부분 수열 크기를 알 수 있다.

result = [0 for _ in range(N)]
for i in range(N):
    result[i] = dp1[i]+dp2[N-i-1] -1

print(max(result))
