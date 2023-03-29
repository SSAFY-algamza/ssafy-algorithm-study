import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline
score_dict = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0, 'C+':2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F':0.0}
total_score = 0
credit = 0

for _ in range(20):
    score = list(input().split())
    if score[2] == 'P':
        continue
    total_score += float(score[1]) * score_dict[score[2]]
    credit += float(score[1])

print(total_score/credit)