N = int(input())
than = input().split()
max_int = 0
min_int = int('9'*(N+1))

def check(arr1, arr2):
    n = len(arr1)
    arr2 = arr2[:n-1]
    for i in range(len(arr2)):
        if arr2[i] == '<':
            if arr1[i] > arr1[i+1]:
                return False
        else:
            if arr1[i] < arr1[i+1]:
                return False
    return True

def choice(depth,choosen):
    global max_int
    global min_int

    if len(choosen) > 1:
        if not check(choosen,than):
            return

    if depth == N+1:
        temp = int(''.join(map(str,choosen)))
        max_int = max(max_int,temp)
        min_int = min(min_int,temp)
        return

    for i in range(10):
        if i not in choosen:
            choosen.append(i)
            choice(depth+1,choosen)
            choosen.pop()

choice(0,[])
print(str(max_int).zfill(N+1))
print(str(min_int).zfill(N+1))