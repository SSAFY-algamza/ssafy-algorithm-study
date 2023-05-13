import sys
input = sys.stdin.readline

N, C = map(int,input().split())
houses = sorted([int(input()) for _ in range(N)])

# 가장 큰 인접거리를 찾으려고 하는데, 이분탐색을 통해서 찾을 예정
s = 1  # 시작점은 1
e = houses[N-1] - houses[0]  # 끝점은 될 수 있는 최대거리인 (마지막 원소-첫원소)
answer = 0  # 나중에 답을 찾으면 할당할 변수 answer

while s <= e:  # 이분 탐색 시작
    mid = (s + e)//2  # 최대거리 찾기 위해 일단 중간값을 기준으로 삼는다.
    current = houses[0]  # 집들 중 가장 첫집을 현재 공유기가 설치된 마지막 집으로 설정하고
    count = 1  # 첫집에 공유기를 설치했으므로 카운팅한다.

    # 이 for 문은 mid가 답이라고 생각하고 일단 공유기를 설치해보는 로직
    for i in range(1, N):  # 두번째집부터 집들을 전부 순회하면서 거리 조건에 적합하다면 공유기를 설치한다
        if houses[i] >= current + mid:  # 다음 집이 (현재 설치된 집+최대인접거리)보다 더 멀리 있으면
            count += 1  # 설치해주고
            current = houses[i]  # 현재 공유기가 설치된 마지막 집을 업데이트해주고

    if count >= C:  # 설치된 개수가 C보다 크거나 같으면
        s = mid+1  # s를 당겨오고
        answer = mid  # 답에 mid를 할당하고
    else:
        e = mid-1  # e를 당겨온다

print(answer)  # while문이 끝나면 answer를 출력  # 근데 시간초과..

'''
N개의 집이 수직선 위에 있음.
각 집의 좌표를 x1 , x2, x3, ... xn 이라고 가정.

이 집들에 공유기 C개를 설치하려고 함(한 집에 두개의 공유기가 들어갈 일은 없음)
인접한 두 공유기 사이의 거리를 가능한 크게 하여 설치하려고 함.

가장 인접한 두 공유기 사이의 거리를 최대로 하는 프로그램을 작성한 후,
가장 인접한 두 공유기 사이의 최대 거리를 출력해야함
'''