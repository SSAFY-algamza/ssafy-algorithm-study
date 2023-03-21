import sys
from collections import defaultdict

def check(dict):
    min_l = 1e9
    max_l = 0
    for i in dict:
        for j in range(len(dict[i]) - K + 1):
            length = dict[i][j + K - 1] - dict[i][j] + 1
            min_l = min(min_l, length)
            max_l = max(max_l, length)
    return (min_l, max_l)

T = int(sys.stdin.readline())
for _ in range(T):
    word = sys.stdin.readline().strip()
    K = int(input())
    dict = defaultdict(list)
    for i in range(len(word)):
        if word.count(word[i]) >= K:
            dict[word[i]].append(i)
    if not dict:
        print(-1)
    else:
        print(*check(dict))
