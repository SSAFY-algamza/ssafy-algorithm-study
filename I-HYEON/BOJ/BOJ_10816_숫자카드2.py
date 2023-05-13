N = int(input())
cards = list(map(int,input().split()))
cards.sort()
M = int(input())
numbers = list(map(int,input().split()))

mydict = {}
for i in range(N):
    mydict[cards[i]] = mydict.get(cards[i],0)+1

for i in range(M):
    if numbers[i] in mydict:
        print(mydict[numbers[i]],end=" ")
    else:
        print(0,end=" ")