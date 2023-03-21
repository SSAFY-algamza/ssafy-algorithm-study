import sys
sys.stdin = open('input.txt')

'''
냅색(Knapsack) 알고리즘

Fractional Knapsack : 물건들을 쪼갤 수 있을 때(ex 거스름돈)
-> Greedy를 활용해 풀면 됨

0-1 Knapsack : 물건들을 쪼갤 수 없을 때
-> DP를 활용해 풀면 됨

1. 배열의 행은 각 물건의 idx 를 의미하고 열은 배낭에 담을 수 있는 무게를 의미하도록 DP 배열을 생성

2. 각 물건들을 순회하며
   만약 물건의 무게 <= 배낭에 담을 수 있는 무게 라면
   1) 현재 물건을 넣었을 때
   2) 현재 물건을 넣지 않고 다른 물건들로 무게를 채웠을 때
   중에서 가치가 큰 경우를 선택해 해당 위치에 입력 (i, W)
   
3. 반드시 마지막 idx에 가장 가치가 큰 경우가 오지 않기 때문에
   한 행에 대한 순회가 끝난 후, rlt 값을 최신화
'''

N, K = map(int, input().split())

DP = [[0] * (K+1) for _ in range(N+1)]
rlt = 0

for i in range(N):
    W, V = map(int, input().split())
    for w in range(1, K+1):
        if W <= w:
            DP[i][w] = max(DP[i-1][w-W] + V, DP[i-1][w])
        else:
            DP[i][w] = DP[i-1][w]
    if rlt <= DP[i][-1]:
        rlt = DP[i][-1]

print(rlt)