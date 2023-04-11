import sys

N, M = map(int, sys.stdin.readline().split())
grid = [[-int(i) for i in sys.stdin.readline().split()] for _ in range(N)]

land_cnt = 0
for r in range(N):
    for c in range(M):
        if grid[r][c] == -1:
            land_cnt += 1
            grid[r][c] = land_cnt
            stack = [(r, c)]
            while stack:
                rr, cc = stack.pop()
                for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    nr, nc = rr+dr, cc+dc
                    if 0 <= nr < N and 0 <= nc < M and grid[nr][nc] == -1:
                        grid[nr][nc] = land_cnt
                        stack.append((nr, nc))

bridges = set()
rep = [i for i in range(land_cnt+1)]

def find_set(rep, x):
    while x != rep[x]:
        x = rep[x]
    return x

for r in range(N):
    a = b = cost= 0
    bridge = False
    for c in range(1, M):
        if not bridge:
            if grid[r][c-1] != 0 and grid[r][c] == 0:
                bridge = True
                a = grid[r][c-1]
                cost += 1
                continue
        
        else:
            if c < M-1 and grid[r][c] == 0:
                cost += 1
                continue
            
            if grid[r][c] != 0:
                bridge = False
                if cost < 2:
                    a = cost = 0
                    continue

                b = grid[r][c]
                bridges.add((cost, a, b))
                a = b = cost = 0

for c in range(M):
    a = b = cost= 0
    bridge = False
    for r in range(1, N):
        if not bridge:
            if grid[r-1][c] != 0 and grid[r][c] == 0:
                bridge = True
                a = grid[r-1][c]
                cost += 1
                continue
        
        else:
            if r < N-1 and grid[r][c] == 0:
                cost += 1
                continue
            
            if grid[r][c] != 0:
                bridge = False
                if cost < 2:
                    a = cost = 0
                    continue

                b = grid[r][c]
                bridges.add((cost, a, b))
                a = b = cost = 0

bridges = sorted(list(bridges))
bridge_cnt = 0
total = 0
for cost, a, b in bridges:
    A, B = find_set(rep, a), find_set(rep, b)
    if A == B:
        continue
    
    bridge_cnt += 1
    total += cost

    if A > B:
        rep[A] = B
    else:
        rep[B] = A 

    if bridge_cnt == land_cnt-1:
        print(total)
        break
else:
    print(-1)
