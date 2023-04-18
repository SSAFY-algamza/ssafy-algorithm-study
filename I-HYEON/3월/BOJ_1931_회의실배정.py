'''
0부터 시작해서 회의를 채워넣는다고 치면
회의가 끝나는 시간이 짧은 것들을 채워넣으면 유리하다.
따라서 모든 회의를 (시작,끝)형태의 튜플로 받아온다음
끝에 들어가는 숫자를 기준으로 정렬한다.
제일 앞에 있는 튜플을 리스트에 넣고, 해당 튜플의 끝보다 크거나 같은 튜플 중에

'''

N = int(input())
meetings = []
for _ in range(N):
    a, b = map(int, input().split())
    meetings.append((a, b))

meetings.sort(key=lambda x:(x[1],x[0]))

ans_list = [meetings[0]]
for i in range(1,N):
    if meetings[i][0] >= ans_list[-1][1]:
        ans_list.append(meetings[i])


print(len(ans_list))