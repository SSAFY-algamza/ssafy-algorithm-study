import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
vote = int(input())
voted_students = list(map(int, input().split()))

picture = []
cnt = []

for i in range(vote):
    if voted_students[i] in picture:
        for j in range(len(picture)):
            if voted_students[i] == picture[j]:
                cnt[j] += 1
    else:
        if len(picture) >= n:
            for j in range(n):
                if cnt[j] == min(cnt):
                    del picture[j]
                    del cnt[j]
                    break
        picture.append(voted_students[i])
        cnt.append(1)

picture.sort()
print(' '.join(map(str, picture)))