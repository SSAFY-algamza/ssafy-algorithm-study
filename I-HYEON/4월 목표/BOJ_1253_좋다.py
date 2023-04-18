N = int(input())
lst = list(map(int, input().split()))

lst.sort()  # 크기 순으로 정렬한다

Good = 0

def is_Good(arr, key):
    global Good
    s, e = 0, len(arr)-1

    while s < e:
        summ = arr[s] + arr[e]

        if summ == key:
            Good += 1
            return
        elif summ < key:
            s += 1
        else:
            e -= 1

for i in range(N):
    new_lst = lst[:i] + lst[i+1:]
    is_Good(new_lst, lst[i])

print(Good)
