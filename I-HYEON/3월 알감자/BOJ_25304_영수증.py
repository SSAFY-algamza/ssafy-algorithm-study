amount = int(input())
count = int(input())

myans = 0
for i in range(count):
    a,b = map(int,input().split())
    myans += a*b

if amount == myans:
    print('Yes')
else:
    print('No')