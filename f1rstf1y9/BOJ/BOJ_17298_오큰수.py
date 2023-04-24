N = int(input())
A = list(map(int, input().split()))

stack = []
ans = []
for i in range(N-1, -1, -1):
    while stack:
        if stack[-1] > A[i]:
            ans.append(stack[-1])
            stack.append(A[i])
            break
        else:
            stack.pop()
    if not len(stack):
        ans.append(-1)
        stack.append(A[i])
print(*ans[::-1])
