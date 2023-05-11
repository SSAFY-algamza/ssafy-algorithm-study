'''
진실 알고 있는 사람 know=[]
파티 참석한 사람 party=[]

지민이 과장 좋아해 -> 파티에 진실 아는 사람 없으면 ? 구라쟁이 | 있으면 ? -> 거짓말쟁이 안알려지고 부풀리는 파티 최대!
'''
import sys
sys.stdin.readline

def find(parent, x):
    if x != parent[x]:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b, know):
    a = find(parent, a)
    b = find(parent, b)

    if a in know and b in know:
        return
    if a in know:
        parent[b] = a
    elif b in know:
        parent[a] = b
    else:
        if a < b:
            parent[b] = a
        else:
            parent[a] = b


n, m = map(int, input().split())
know = list(map(int, input().split()))[1:]

party=[]
parent=list(range(n+1))

for _ in range(m):
    party_info = list(map(int, input().split()))
    party_len = party_info[0]
    p = party_info[1:]
    
    for i in range(party_len - 1):
        union(parent, p[i], p[i+1], know)
    
    party.append(p)
    
ans = 0
for p in party:
    for i in range(len(p)):
        if find(parent, p[i]) in know:
            break
    else:
        ans += 1

print(ans)

