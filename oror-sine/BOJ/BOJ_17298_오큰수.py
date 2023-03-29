import sys

N = int(sys.stdin.readline())
sequence = [int(i) for i in sys.stdin.readline().split()]
maxi = sequence[-1]
NGEs = [sequence[-1]]
ans = [-1]
for idx in range(2, N + 1):
    if maxi <= sequence[-idx]:
        maxi = sequence[-idx]
        ans.append(-1)
        NGEs = [sequence[-idx]]
        continue
    for _ in range(len(NGEs)):
        if sequence[-idx] < NGEs[-1]:
            ans.append(NGEs[-1])
            NGEs.append(sequence[-idx])
            break
        NGEs.pop()

print(" ".join(map(str, ans[::-1])))
