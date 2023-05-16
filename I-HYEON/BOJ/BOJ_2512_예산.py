N = int(input())
budgets = list(map(int,input().split()))
max_sum_budget = int(input())
answer = 0

if sum(budgets) <= max_sum_budget:  # 합이 총 예산액보다 작거나 같으면
    print(max(budgets))  # 제일 큰 값을 프린트
else:
    s = 1
    e = max_sum_budget

    while s<=e:
        mid = (s+e)//2

        passed_budgets_sum = 0
        for i in budgets:  # 순회하면서 상한액 조건에 맞게 값을 변형한 후 합침
            if i > mid:
                passed_budgets_sum += mid
            else:
                passed_budgets_sum += i

        if passed_budgets_sum > max_sum_budget:  # 총 예산액을 넘어버렸다면, 상한액을 줄여야하므로
            e = mid-1
        else:
            answer = mid
            s = mid+1

    print(answer)