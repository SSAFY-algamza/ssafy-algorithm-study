import sys
N = int(sys.stdin.readline())
people = [[int(i) for i in sys.stdin.readline().split()] for _ in range(N)]
ranks = [1] * N
for i in range(N):
    for j in range(i, N):
        if people[i][0] > people[j][0] and people[i][1] > people[j][1]:
            ranks[j] += 1
        elif people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            ranks[i] += 1
print(*ranks)
