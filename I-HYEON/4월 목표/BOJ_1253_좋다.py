from itertools import combinations

N = int(input())
lst = list(map(int, input().split()))

lst.sort()  # 크기 순으로 정렬한다

Good = 0
for i in range(N):
    if i >= 2:
        temp_lst = lst[::]
        temp_lst.pop(i)
        Good_list = list(set(map(lambda x:sum(x),list(combinations(temp_lst, 2)))))
        print(Good_list)
        if lst[i] in Good_list:
            print(lst[i])
            Good += 1
print(Good)