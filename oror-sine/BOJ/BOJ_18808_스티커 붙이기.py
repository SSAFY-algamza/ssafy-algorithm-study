import sys
N, M, K = map(int, sys.stdin.readline().split())
laptop = [[0]*M for _ in range(N)]

def rotate(R, C, sticker):
    new_sticker = [[0]*R for _ in range(C)]
    
    for r in range(R):
        for c in range(C):
            new_sticker[c][R-r-1] = sticker[r][c]

    return new_sticker

for _ in range(K):
    R, C = map(int, sys.stdin.readline().split())
    sticker = [[int(i) for i in sys.stdin.readline().split()] for _ in range(R)]
    found = False
    for _ in range(4):
        for t in range(N-R+1):
            for l in range(M-C+1):
                found = True
                for r in range(R):
                    for c in range(C):
                        if sticker[r][c] and laptop[t+r][l+c]:
                            found = False
                            break
                
                    if not found: break
                if not found: continue
                    
                for r in range(R):
                    for c in range(C):
                        if sticker[r][c]:
                            laptop[t+r][l+c] = sticker[r][c]
                        
                if found: break
            if found: break
        if found: break
        sticker = rotate(R, C, sticker)
        R = len(sticker)
        C = len(sticker[0])
    
ans = 0
for row in laptop:
    ans += sum(row)
print(ans)
