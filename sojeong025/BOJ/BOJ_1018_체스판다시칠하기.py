n, m = map(int, input().split())

chess = []
cnt = []

for _ in range(n):
    chess.append(input())


for i in range(n-7):
    for j in range(m-7):
        black = 0
        white = 0
        for k in range(i, i+8):
            for l in range(j, j+8):
                if (k + l) % 2 == 0:
                    if chess[k][l] != 'B':
                        black += 1
                    if chess[k][l] != 'W':
                        white += 1
                
                else:
                    if chess[k][l] != 'W':
                        black += 1
                    if chess[k][l] != 'B':
                        white += 1
                    
        cnt.append(black)
        cnt.append(white)

print(min(cnt))