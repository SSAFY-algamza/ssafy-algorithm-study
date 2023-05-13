import sys
input = sys.stdin.readline

N, M = map(int,input().split())  # 전체 나무의 개수와 상근이가 필요한 나무길이
tree_height_list = list(map(int,input().split()))

def is_ok(height):
    result = 0
    for i in range(N):
        if tree_height_list[i] > height:
            result += tree_height_list[i]-height
    if result >= M:
        return True
    return False

s = 1
e = max(tree_height_list)-1
answer = 0
while s <= e:
    mid = (s+e)//2

    if is_ok(mid):
        answer = mid
        s = mid+1

    else:
        e = mid-1

print(answer)
