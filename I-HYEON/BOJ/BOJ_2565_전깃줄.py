N = int(input())
arr = [0 for _ in range(501)]
dp = [1 for _ in range(501)]

for _ in range(N):
    a,b = map(int,input().split())
    arr[a] = b

for i in range(1,501):
    if arr[i] == 0:  # 원소가 0이면 전깃줄이 없는 것이므로 볼 필요가 없음
        continue
    for j in range(1,i):
        if arr[j] == 0:  # 마찬가지
            continue
        if arr[i] > arr[j]: # 원소가 앞에 있는 원소들을 순회하면서 그 뒤에 붙을 수 있는지 확인
            dp[i] = max(dp[i],dp[j]+1)

print(N-max(dp))