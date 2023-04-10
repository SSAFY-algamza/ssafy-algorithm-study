'''
A 수열의 길이 N과 A 수열의 각각의 원소가 주어짐
이를 토대로 비내림차순인 수열 P를 만드는게 목표

A 수열과 같은 길이의 수열 P를 만들고
수열 A의 작은 값의 인덱스와 같은 위치의 수열 P에 0부터 N-1 까지 넣어주면 된다
'''
N = int(input())
A_lst = list(map(int, input().split()))
sorted_A = sorted(A_lst)

# 수열 A와 같은 길이의 수열 P 만들기
lst_P = [0] * N

for i in range(N):
    idx = sorted_A.index(A_lst[i])
    lst_P[i] = idx
    sorted_A[idx] = -1

print(*lst_P)