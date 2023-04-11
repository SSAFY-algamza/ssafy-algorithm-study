def bt(n, idx):
    if n == 6:
        print(*stack)
        return
    for i in range(idx, k):
        if lst[i] not in stack:
            stack.append(lst[i])
            bt(n+1, i+1)
            stack.pop()

while True:
    nums = list(map(int,input().split()))
    if nums[0] == 0:
        break
    k, *lst = nums
    stack = []
    bt(0, 0)
    print()
