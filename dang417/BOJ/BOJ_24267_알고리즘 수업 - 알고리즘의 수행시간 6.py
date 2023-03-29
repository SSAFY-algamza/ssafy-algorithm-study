n = int(input())

rlt = 0
num = n-2
for i in range(1, n-1):
    rlt += num * i
    num -= 1

print(rlt)
print(3)