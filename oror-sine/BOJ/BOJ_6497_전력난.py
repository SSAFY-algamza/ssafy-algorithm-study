import sys
readline = sys.stdin.readline

def find(rep, x):
    while x != rep[x]:
        x = rep[x]
    return x

while True:
    m, n = map(int, readline().split())
    if m == 0 and n == 0 : break

    rep = list(range(m))
    edges = []
    cnt = 1 
    cost = 0
    
    for _ in range(n):
        x, y, z = map(int, readline().split())
        edges.append((x, y, z))
        cost += z

    edges.sort(key = lambda edge: edge[2])

    for x, y, z in edges:
        A, B = find(rep, x), find(rep, y)
        
        if A == B: continue
        
        if A > B: rep[A] = B
        else: rep[B] = A
        
        cnt += 1
        cost -= z
        
        if cnt == m: break

    print(cost)
