N,K = map(int,input().split())

result = []
for n in range(1,N+1):
    if N % n == 0:  # 나머지가 0이면
        result.append(n)  # 그 때의 분모가 약수이므로 어펜트

if len(result) < K:
    ans = 0
else:
    ans = result[K-1]

print(ans)