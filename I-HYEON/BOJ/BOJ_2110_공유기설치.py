import sys
input = sys.stdin.readline

N, C = map(int,input().split())
houses = sorted([int(input()) for _ in range(N)])

def is_ok(num):
    current = houses[0]  # 집들 중 가장 첫집을 현재 공유기가 설치된 마지막 집으로 설정하고
    count = 1  # 첫집에 공유기를 설치했으므로 카운팅한다.

    for i in range(1, N):  # 두번째집부터 집들을 전부 순회하면서 거리 조건에 적합하다면 공유기를 설치한다
        if houses[i] >= current + num:  # 다음 집이 (현재 설치된 집 + 최대인접거리)보다 더 멀리 있으면
            count += 1  # 설치해주고
            current = houses[i]  # 현재 공유기가 설치된 마지막 집을 업데이트해주고

            if count > C:
                return True

    if count == C:
        return True
    return False

# 가장 큰 인접거리를 찾으려고 하는데, 이분탐색을 통해서 찾을 예정
s = 1  # 시작점은 1
e = houses[N-1] - houses[0]  # 끝점은 될 수 있는 최대거리인 (마지막 원소-첫원소)
answer = 0  # 나중에 답을 찾으면 할당할 변수 answer

while s <= e:  # 이분 탐색 시작
    mid = (s + e)//2  # 최대거리 찾기 위해 일단 중간값을 기준으로 삼는다.

    if is_ok(mid):
        s = mid+1  # s를 당겨오고
        answer = mid  # 답에 mid를 할당하고
    else:
        e = mid-1  # e를 당겨온다

print(answer)