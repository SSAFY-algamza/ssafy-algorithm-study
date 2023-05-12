import sys
input = sys.stdin.readline

N, M = map(int,input().split())

dict_lst = ['',]
for _ in range(N):
    dict_lst.append(input().rstrip())

for _ in range(M):
    quest = input().rstrip()

    if quest.isdigit():
        print(dict_lst[int(quest)])
    else:
        print(dict_lst.index(quest))