import sys
sys.stdin = open('input.txt')

N = int(input())
meeting = []
for _ in range(N):
    S, E = map(int, input().split())
    meeting.append((S, E))

meeting.sort(key=lambda x: (x[1], x[0]))
end_time = 0
cnt = 0
for S, E in meeting:
    if S >= end_time:
        end_time = E
        cnt += 1
print(cnt)
