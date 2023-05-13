import sys
input = sys.stdin.readline

N, M = map(int,input().split())

dict_lst = ['',]
for _ in range(N):
    dict_lst.append(input().rstrip())

ans_lst = []
for _ in range(M):
    quest = input().rstrip()

    if quest.isdigit():
        ans_lst.append(dict_lst[int(quest)])
    else:
        ans_lst.append(dict_lst.index(quest))

print("/n".join(ans_lst))