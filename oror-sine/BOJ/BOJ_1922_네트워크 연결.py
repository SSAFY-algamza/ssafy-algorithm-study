import sys, heapq  ## 최솟값을 가져올 때, sort 하는 것보다 heapq를 사용하는게 빠른 듯 함 
readline = sys.stdin.readline  # function call할 때면 __getattribute__()나 __getattr__()을 호출하게되는데 이 time cost를 줄일 수 있다.
N = int(readline())
M = int(readline())
wires = []
for _ in range(M):
    a, b, c = map(int, readline().split())
    heapq.heappush(wires, (c, a, b)) 
reps = list(range(N+1))  ## [i for i in range(N+1)] 보다 빠른 듯

def find_set(reps, x):
    while x != reps[x]:
        x = reps[x]
    return x

ans = 0
cnt = 1  # 매 loop 조건문에서 N-1 연산하면 연산량이 증가하므로 
for _  in range(M):
    c, a, b = heapq.heappop(wires)
    A, B = find_set(reps, a), find_set(reps, b)
    
    if A == B: continue
    
    if A < B: reps[A] = B  #
    else: reps[B] = A
    
    cnt += 1
    ans += c
    
    if cnt == N: break  # 최소신장트리의 간선의 갯수는 N-1
    
print(ans)