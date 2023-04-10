def quicksort(arr,s,e):
    if s<e:
        pivot = partition(arr,s,e)
        quicksort(arr,s,pivot-1)
        quicksort(arr,pivot+1,e)

def partition(arr, s, e):

    pivot = arr[s][0]
    i = s
    j = e

    while i <= j:
        while i<=j and arr[i][0] <= pivot:
            i += 1

        while i<=j and arr[j][0] >= pivot:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[s], arr[j] = arr[j], arr[s]
    return j

N = int(input())

lst = []
for _ in range(N):
    a,b = input().split()
    a = int(a)
    lst.append((a,b))

quicksort(lst,0,N-1)

for l in lst:
    print(*l)