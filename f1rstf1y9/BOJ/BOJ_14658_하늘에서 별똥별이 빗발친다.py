N, M, L, K = map(int, input().split())

def count_stars(y,x):
    cnt = 0
    for s in shooting_stars:
        if y <= s[0] <= y+L and x <= s[1] <= x+L:
            cnt += 1
    return cnt

shooting_stars = []
max_shoot = 0
for _ in range(K):
    x, y = map(int, input().split())
    shooting_stars.append((x,y))

for a in shooting_stars:
    for b in shooting_stars:
        y, x = a[0], b[1]
        cnt = count_stars(y,x)
        max_shoot = max(max_shoot, cnt)
print(K-max_shoot)