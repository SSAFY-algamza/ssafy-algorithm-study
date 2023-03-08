import sys
sys.stdin = open('input.txt')

T = int(input())
for _ in range(T):
    n = int(input())
    parent = [0] * (n+1)
    for _ in range(n-1):
        A, B = map(int, input().split())
        parent[B] = A

    child1, child2 = map(int, input().split())
    p_ch1, p_ch2 = [child1], [child2]

    while parent[child1]:
        p_ch1.append(parent[child1])
        child1 = parent[child1]

    while parent[child2]:
        p_ch2.append((parent[child2]))
        child2 = parent[child2]

    while p_ch1 and p_ch2 and p_ch1[-1] == p_ch2[-1]:
        answer = p_ch1.pop()
        p_ch2.pop()

    print(answer)
