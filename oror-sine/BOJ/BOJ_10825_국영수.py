import sys
N = int(sys.stdin.readline())
scores = []
for i in range(N):
    name, k, e, m = sys.stdin.readline().split()
    scores.append((name, int(k), int(e), int(m)))
scores.sort(key= lambda score: score[0])
scores.sort(key= lambda score: score[3], reverse=True)
scores.sort(key= lambda score: score[2])
scores.sort(key= lambda score: score[1], reverse=True)
for score in scores:
    print(score[0])