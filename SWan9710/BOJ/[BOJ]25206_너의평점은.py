score = {
'A+' : 4.5,
'A0' : 4.0,
'B+' : 3.5,
'B0' : 3.0,
'C+' : 2.5,
'C0' : 2.0,
'D+' : 1.5,
'D0' : 1.0,
'F' : 0.0,
}
total_grade = 0
total_score = 0
for i in range(20):
    word, grade, rank = input().split()

    if rank != 'P':
        total_score += score[rank] * float(grade)
        total_grade += float(grade)
    else:
        continue

print(total_score / total_grade)