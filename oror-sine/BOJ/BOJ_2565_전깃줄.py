import sys
N = int(sys.stdin.readline())
wires = sorted([[int(i) for i in sys.stdin.readline().split()] for _ in range(N)])  # [A의 위치, B의 위치]를 담은 오름차순 리스트
dp = [1]*N  # 해당 인덱스의 전선을 반드시 포함할 때, 0번 인덱스부터 해당 인덱스까지 겹치지 않는 전선의 최대 갯수
for i in range(N):
    if nonoverlapping := [j for j in range(i) if wires[i][1] > wires[j][1]]:  # 안 겹치는 전선 리스트가 있다면
        dp[i] = dp[max(nonoverlapping, key=lambda x: dp[x])] + 1  # 안 겹치는 전선 중 dp 최대 값의 + 1
print(N-max(dp)) # 없애야 하는 전깃줄 = 총 전선 수 - 안 겹치는 최대 전선 수
