import sys
from collections import deque
T = int(sys.stdin.readline())
for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    cnts = [0]*9
    documents = deque([])
    for i, importance in enumerate(sys.stdin.readline().split()):
        documents.append((i, int(importance)))
        cnts[documents[-1][-1]-1] += 1
    cnt = 0
    while True:
        document = documents.popleft()
        for i in range(document[-1], 9):
            if cnts[i]:
                documents.append(document)
                break
        else:
            cnt += 1
            cnts[document[-1]-1] -= 1
            if document[0] == M:
                print(cnt)
                break
