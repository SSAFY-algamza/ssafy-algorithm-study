from collections import deque

N,M = map(int,input().split())
cards = sorted(list(map(int,input().split())))

start = deque([])
gap = M

def backtrack(depth,chosen,result):
    global gap

    if depth == 3:
        temp = M - result
        if gap > temp:
            gap = temp  # 갱신

    if not chosen:
        start = 0
    else:
        start = cards.index(chosen[-1])+1
    for i in range(start,N):

        if result+cards[i] > M:
            return

        if i not in chosen:

            chosen.append(cards[i])
            backtrack(depth+1,chosen,result+cards[i])
            chosen.pop()

backtrack(0,start,0)
print(M-gap)