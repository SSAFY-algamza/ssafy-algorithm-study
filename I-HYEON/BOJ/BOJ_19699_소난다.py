N, M = map(int,input().split())
cows = list(map(int,input().split()))
visited = [0 for _ in range(N)]
ans = set()

def prime_check(num):  # prime 인지 판별하는 함수

    for i in range(2,num):
        if num%i:
            continue
        else:
            return False
    return True

def backtrack(depth, choosen, total):

    if depth == M:
        if prime_check(total):
            ans.add(total)
        return

    if choosen:
        start = choosen[-1] + 1
    else:
        start = 0
    for i in range(start, N):
        if not visited[i]:  # 아직 사용 안 한 원소라면
            visited[i] = 1  # 방문 표시해주고
            choosen.append(i)
            total += cows[i]  # 해당 소의 무게를 더해준다
            backtrack(depth+1, choosen, total)
            total -= cows[i]
            choosen.pop()
            visited[i] = 0

backtrack(0, [], 0)

temp = sorted(list(ans))
if temp:
    print(*temp)
else:
    print(-1)