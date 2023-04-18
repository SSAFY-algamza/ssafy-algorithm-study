import sys
N = int(sys.stdin.readline())
R = int(sys.stdin.readline())
seq = [int(i) for i in sys.stdin.readline().split()]

frames = {}
for i, student in enumerate(seq):
    if student in frames:
        frames[student][0] += 1
    else:
        if N > 0:
            N -= 1
        else:
            gone = sorted(frames.keys(), key=lambda student: frames[student])[0]
            del frames[gone]
        frames[student] = [1, i]
        
for student in sorted(frames.keys()):
    print(student, end=' ')