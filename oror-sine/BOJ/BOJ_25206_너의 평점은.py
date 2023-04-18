import sys
readline = sys.stdin.readline
total_credit = 0
total_score = 0
scores = {
    "A+":4.5,
    "A0":4.0,
    "B+":3.5,
    "B0":3.0,
    "C+":2.5,
    "C0":2.0,
    "D+":1.5,
    "D0":1.0,
    "F":0.0,
    "P":-1
    }

for _ in range(20):
    _, credit, score = readline().split()
    score = scores[score]
    if score == -1:
        continue
    credit = int(credit[0])
    total_credit += credit
    total_score += score * credit

print(total_score/total_credit)
