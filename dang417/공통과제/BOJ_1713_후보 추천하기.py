import sys
sys.stdin = open('input.txt')

N = int(input())
total_recommend = int(input())
recommendations = list(map(int, input().split()))

picture = []
recommend_cnt = []

for i in range(total_recommend):
    if recommendations[i] in picture:
        for j in range(len(picture)):
            if recommendations[i] == picture[j]:
                recommend_cnt[j] += 1
    else:
        if len(picture) >= N:
            for j in range(N):
                if recommend_cnt[j] == min(recommend_cnt):
                    del picture[j]
                    del recommend_cnt[j]
                    break
        picture.append(recommendations[i])
        recommend_cnt.append(1)

print(*sorted(picture))