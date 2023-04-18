N = int(input())
M = int(input())
students = list(map(int, input().split()))

def get_least():
    min_v = M
    res = 0
    for c in cur:
        if photo[c] < min_v:
            min_v, res = photo[c], c
    return res

photo = {}
cur = []
idx = 0
for s in students:
    if len(cur) >= N and not photo.get(s, 0):
        d = get_least()
        photo[d] = 0
        photo[s] = 1
        cur.remove(d)
        cur.append(s)
    else:
        if s not in cur:
            cur.append(s)
        photo[s] = photo.get(s, 0) + 1

print(*sorted(cur))
