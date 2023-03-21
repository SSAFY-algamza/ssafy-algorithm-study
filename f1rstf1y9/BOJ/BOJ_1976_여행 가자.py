def get_parent(n):
    if parents[n] != n:
        parents[n] = get_parent(parents[n])
    return parents[n]

def union(a, b):
    a, b = get_parent(a), get_parent(b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b

N = int(input())
M = int(input())
parents = [i for i in range(N)]
for i in range(N):
    nums = list(map(int, input().split()))
    for j in range(N):
        if nums[j]:
            union(i, j)
plan = list(map(int, input().split()))

parents = [0] + parents
p = parents[plan[0]]
for i in plan[1:]:
    if parents[i] != p:
        print("NO")
        break
else:
    print("YES")
