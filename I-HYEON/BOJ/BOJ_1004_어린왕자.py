import math

T = int(input())

for tc in range(1,T+1):
    sx,sy,ex,ey = map(int,input().split())
    P = int(input())
    cnt = 0
    for _ in range(P):
        px,py,r = map(int,input().split())
        s_distance = math.sqrt((px-sx)**2+(py-sy)**2)  # 출발점과 특정 행성 중심점 간의 거리
        e_distance = math.sqrt((px-ex)**2+(py-ey)**2)  # 도착점과 특정 행성 중심점 간의 거리
        if s_distance < r and e_distance > r:  # 출발점이 원 안에 있는데 도착점은 원밖에 있을 때
            cnt += 1
        if e_distance < r and s_distance > r:  # 도착점은 원 안에 있는데 출발점은 원밖에 있을 때
            cnt += 1
    print(cnt)