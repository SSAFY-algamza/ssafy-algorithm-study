def change(gender,key):
    if gender == 1:  # 남자 일 때
        for b in range(1,N+1):  # 인덱스 0은 패스하고 1부터 검토
            if not b%key:  # 배열의 인덱스(즉, 스위치번호)가 key의 배수이면 반전시켜줘
                if on_off[b] == 0:
                    on_off[b] = 1
                elif on_off[b] == 1:
                    on_off[b] = 0

    elif gender == 2:  # 여자 일 때

        if on_off[key] == 0:  # 일단 key번호 스위치 상태부터 무조건 반전시켜주고
            on_off[key] = 1
        elif on_off[key] == 1:
            on_off[key] = 0

        for g in range(1,N):  # 대칭검사에 이용
            left = key - g
            right = key + g
            if 0<left<=N and 0<right<=N:  # 인덱스를 벗어나지 않으면 겈토
                if on_off[left] == on_off[right]:  # 대칭이라면 반전시켜줘
                    if on_off[left] == 0:
                        on_off[left] = 1
                    elif on_off[left] == 1:
                        on_off[left] = 0
                    if on_off[right] == 0:
                        on_off[right] = 1
                    elif on_off[right] == 1:
                        on_off[right] = 0
                else:  # 대칭이 아니라면 stop
                    break
            else:  # 하나라도 인덱스에서 벗어나면 그냥 바로 break
                break
    return


N = int(input())  # 스위치 개수
on_off = [0 for _ in range(N+1)]  # 인덱스랑 스위치번호를 일치시킬 수있게 n+1 배열 생성
info = [0] + list(map(int,input().split()))  # 스위치 상태 정보 앞에 0 을 붙여 할당
for i in range(len(info)):
    on_off[i] = info[i]

M = int(input())  # 사람 수
for m in range(M):  # 사람 수 만큼 입력 받아오기
    g,k = map(int,input().split())
    change(g,k)

# 최종 스위치 상태를 출력
ans = on_off[1:]
if len(ans) > 20:  # 길이가 20이 넘으면
    for l in range(0,len(ans),20):  # 20개씩 끊어 출력
        try:
            print(*ans[l:l+20])
        except:
            print(*ans[l:])
else:
    print(*ans)