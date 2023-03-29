n = int(input())

for _ in range(n):
    password=input()
    left = []
    right = []

    for i in password:
        if i == ">":
            if right:
                left.append(right.pop())
        elif i =="<":
            if left:
                right.append(left.pop())
        elif i =="-":
            if left:
                left.pop()
        else:
            left.append(i)
    print("".join(left)+"".join(reversed(right)))

