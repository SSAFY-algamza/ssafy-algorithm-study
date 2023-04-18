N = int(input())

arr = sorted([list(map(int, input().split()))for _ in range(N)], key=lambda x:(x[1],x[0]))

for i in arr:
    print(*i)