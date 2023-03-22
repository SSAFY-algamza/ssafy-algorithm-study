import sys
N = int(sys.stdin.readline())
sequence = []
counter = {}
max_cnt = 0
mosts = []
for _ in range(N):
    num = int(sys.stdin.readline())
    sequence.append(num)
    if num in counter:
        counter[num] += 1
    else:
        counter[num] = 1
    if max_cnt < counter[num]:
        max_cnt = counter[num]
        mosts = [num]
    elif max_cnt == counter[num]:
        mosts.append(num)
sequence.sort()
mosts.sort()
ans = []
ans.append(round(sum(sequence)/N))
ans.append(sequence[N//2])
ans.append(mosts[1] if len(mosts) > 1 else mosts[0])
ans.append(sequence[-1] - sequence[0])
print(*ans, sep="\n")
