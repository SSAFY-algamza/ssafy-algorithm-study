import sys
input = sys.stdin.readline

K, N = map(int, input().split())  # K는 주어진 랜선의 개수, N은 필요한 랜선 개수(만들어내야하는 개수)
lengths = [int(input()) for _ in range(K)]
lengths.sort()

# 최대 랜선 길이는 아무리 짧아도 1이고, 아무리 길어도 주어진 길이들 중 최대길이
# 위의 범위를 이분탐색으로 줄여나가면서 조건을 충족하는 길이를 정하면 된다.

'''
예를 들어, 첫 기준은 1과 802의 중간값인 401이다
최대 랜선의 길이가 401이면 리스트를 돌면서 401만큼 가능한 한 다 잘랐을 때, 랜선 개수가 N보다 많으면 적합한 것이 된다.
많으면 일단 답을 업데이트는 하는데, 더 큰수도 가능할 수 있으니까 s를 mid+1로 옮겨준다.

랜선 개수가 N보다 작으면 아무리 잘라도 조건을 충족할 수 없다는 뜻이고 해당 미드값은 기각된다.
길이를 줄여야한다는 의미이므로 e를 mid-1로 옮겨서 다시 시행한다.
'''

def isPossible(len):
    cnt = 0
    for length in lengths:
        cnt += length//len
    return cnt

ans = 0
s = 1
e = lengths[K-1]
while s <= e:
    mid = (s+e)//2

    temp = isPossible(mid)

    if temp >= N:
        ans = mid
        s = mid+1
    else:
        e = mid-1

print(ans)