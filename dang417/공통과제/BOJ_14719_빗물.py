H, W = map(int, input().split())
heights = list(map(int, input().split()))

rlt = 0
for i in range(1, W - 1):
    maxV = min(max(heights[:i]), max(heights[i+1:]))

    if heights[i] < maxV:
        rlt += maxV - heights[i]

print(rlt)