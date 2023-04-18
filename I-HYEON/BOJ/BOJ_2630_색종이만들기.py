N = int(input())
paper = [list(map(int,input().split())) for _ in range(N)]
white = 0
blue = 0

def check(r, c, n):  # r은 가장 첫번째 행 번호, c는 가장 첫번째 열 번호, n은 총 길이
    global white
    global blue

    color = paper[r][c]
    for i in range(n):
        for j in range(n):  # 전체 배열을 순회 하면서 색깔이 바뀌는지 체크
            if paper[r+i][c+j] != color:  # 색깔이 바뀌었다면
                check(r, c, n//2)  # 1번 영역 재귀
                check(r, c+n//2, n//2)  # 2번 영역 재귀
                check(r+n//2, c, n//2)  # 3번 영역 재귀
                check(r+n//2, c+n//2, n//2)  # 4번 영역 재귀
                return
    else:
        if color == 0:
            white += 1
        else:
            blue += 1


check(0,0,N)
print(white)
print(blue)