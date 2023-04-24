'''
구현 아이디어
1. 일단 시킨대로 하자
R -> 배열 뒤집기
D -> 배열의 제일 앞 버리기
--------------------시간초과--------------------------
why? 배열 뒤집기와 배열 제일 앞을 버리면 그 연산을 수행 후 배열을 재정렬 해야하는데
이 때 배열의 갯수가 최대 100000개 이다보니 R 이나 D 가 입력받아 올때마다 뒤집고 버리면
매번 최대 100000만번의 작업을 수행하다보니 시간초과 발생
------------------------------------------------------
1. R 갯수 세기
- R이 100개가 오든 101개가 오든 결국 배열을 뒤집는 역할만 하기에 갯수를 세서 2로 나눠주기
- 홀수 >> 배열 뒤집고 작업
- 짝수 >> 배열 안뒤집고 작업

2. R 이 홀이냐 짝이냐에 따라서 문자열 제거위치 변경해주기
- 홀수 >> 문자열 뒤에서 제거 >> 뒤집고 앞에서 빼는거와 작업 동일
- 짝수 >> 문자열 앞에서 제거

3. 출력전 R이 홀이냐 짝이냐에 따러서 출력방향 정해주기
- 홀수 >> 뒤집어서 출력
- 짝수 >> 똑바로 출력

4. 출력할때 deque() 제거 해주기
join 함수 써서 출력
join 할때 사이사이에 , 들어가야 하니 ','.join(arr)
마지막으로 앞뒤에 '[' , ']' 넣어주기 

'''
from collections import deque
import sys

T = int(input())
for tc in range(T):
    # 입력때 보니 오른쪽에 띄워쓰기 있어서 제거해줌
    P = sys.stdin.readline().rstrip()
    N = int(input())
    # [ ] 제거해서 입력받기 위해 슬라이싱해서 들고오기 구분자는 쉼표이고 오른쪽 띄워쓰기 제거
    arr = deque(sys.stdin.readline().rstrip()[1:-1].split(','))
    # 처음부터 빈 배열로 입력이 오면 배열에 [ ] 있는걸로 들어와짐
    # 그래서 0 이면 배열 초기화 해주기
    if N == 0:
        arr = deque()

    # R 갯수 세주기
    count_R = 0
    for word in P:
        if word == 'R':
            count_R += 1

        # D 입력 받았는데 배열이 있는경우
        else:
            if arr:
                # 정배열
                if count_R % 2 == 0:
                    arr.popleft()

                # 역배열
                else:
                    arr.pop()

            # D 입력에 배열이 없는경우
            else:
                print('error')
                break
    # for - else 조건 break 에 걸리지 않았다면 아래코드 실행
    else:
        if count_R % 2 == 0:
            # print('[',end='')
            # print(','.join(arr),end='')
            # print(']')
            print('[' + ','.join(arr) + ']')
        else:
            arr.reverse()
            # print('[', end='')
            # print(','.join(arr), end='')
            # print(']')
            print('[' + ','.join(arr) + ']')
