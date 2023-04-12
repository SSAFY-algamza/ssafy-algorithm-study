import sys
sys.stdin = open("input.in","r")

keyboard = ['qwertyuiop', 'asdfghjkl ', 'zxcvbnm   ']
l_position = (0,0)
r_position = (0,0)

l, r = input().split()
words = input()

for i in range(3):
    for j in range(10):

        if keyboard[i][j] == l:
            l_position = (i,j)
        if keyboard[i][j] == r:
            r_position = (i,j)


ans = 0
for w in words:

    for i in range(3):
        for j in range(10):

            if w == keyboard[i][j]:
                ans += 1
                if ( i == 0 and j <= 4 ) or (i == 1 and j <=4 ) or (i ==2 and j <=3):
                    ans += abs(l_position[0]-i) + abs(l_position[1]-j)
                    l_position = (i,j)
                else:
                    ans += abs(r_position[0]-i) + abs(r_position[1]-j)
                    r_position = (i, j)

print(ans)