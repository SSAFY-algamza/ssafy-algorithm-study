import sys
input = sys.stdin.readline

N, A = map(int,input().split())
lst = [list(map(int,input().split())) for _ in range(N)]
answer = 0  # 최대hp의 최소값을 일단 0으로 초기화
start, end = 1, N*int(1e6)*int(1e6)

def can_clear(curATK,maxHP):
    curHP = maxHP
    for type, atk, hp in lst:
        if type == 1:
            temp = hp//curATK if not hp%curATK else hp//curATK+1
            curHP -= atk * (temp-1)
        else:
            curATK += atk
            curHP = min(maxHP,curHP + hp)
        if curHP <= 0:
            return False
    return True

while start <= end:
    mid = (start+end)//2
    if can_clear(A,mid):
        end = mid -1
        answer = mid
    else:
        start = mid + 1

print(answer)