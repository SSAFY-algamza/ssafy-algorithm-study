# X, [A, B, C, D] 나중에 인덱스로 A ~ D에 접근하기 위함.
X, *ABCD = map(int, input().split())

# `idx`센트를 만들 수 있을 때` `총 동전`의 수가 최대가 되는 `1센트`, `5센트`, `10센트`, `25센트` 및 `총 동전`의 개수
dp = [[0, 0, 0, 0, 0]]

# 동전 단위들, 인덱스로 접근하기 위한 읽기 전용 값
units = (1, 5, 10, 25)


# dp[idx]를 구하는 함수
def Coins(idx):
    # 초기 값: [A, B, C, D, -1]   # 모든 동전을 다 써도(A, B, C, D) 만들 수 없다(-1)
    coins = [*ABCD, -1]
    
    # 각 동전 단위에 대하여 
    for i, unit in enumerate(units):
        if idx < unit: break  # 단위만큼 뺐을 때, 인덱스가 음수가 되는 경우
        if dp[idx-unit][i] == ABCD[i]: continue # 해당 동전을 다 쓴 경우

        # 해당 단위의 동전이 남아있으면, 복사한 뒤 동전추가
        tmp = [*dp[idx-unit]]
        tmp[i] += 1
        tmp[-1] += 1

        # 총 동전 수가 더 많은 coins로 갱신
        if coins[-1] < tmp[-1]:
            coins = tmp

    return coins


for x in range(1, X+1):
    dp.append(Coins(x))

if dp[X][-1] == -1 : print(0, 0, 0, 0)
else: print(*dp[X][:4])
