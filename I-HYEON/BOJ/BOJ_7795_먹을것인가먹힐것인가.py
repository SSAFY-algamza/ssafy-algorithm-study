'''
A의 원소를 순회한다. 하나를 가져왔을때, 다시 B를 순회하면서 작은 애가 있으면 카운트한다. -> 시간초과

A와 B를 오름차순으로 정렬한다. A는 순서대로 순회하고 B는 거꾸로 순회하면서, 시간을 줄인다.
'''

test_case = int(input())
for _ in range(test_case):
    a, b = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    A.sort(reverse=True)
    B.sort(reverse=True)

    cnt, ai, bi = 0, 0, 0
    while ai < a:
        if A[ai] > B[bi]:
            cnt += b-bi
            ai += 1
        else:
            if bi == b-1:
                ai += 1
                continue
            bi += 1

    print(cnt)