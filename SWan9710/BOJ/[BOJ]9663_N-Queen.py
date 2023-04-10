'''
퀸이 0, 0 에 위치할 경우
가로 0, 세로 0 대각선, 퀸 주변 델타8범위 둘수 없음

4 * 4 체스판에서 최대로 둘 수 있는 퀸의 갯수
X O X X
X X X O
O X X X
X X O X
형태가 최대로 둘 수 있는 모양
한줄에 최대 1개만 둘 수 있음
즉 N의 갯수만큼 퀸을 두었을 때 최대갯수임

조건
1. 한줄에 1개만 놓고 다음줄에 놓으러 내려갈건데 j 위치에 겹치는 퀸이 있는경우 넘어가기
2. 대각선에 있을경우 넘어가기
3. 탐색은 1줄에 N 번 탐색
4. 종료조건은 퀸을 N개 두었을 때
'''

def DFS(count):
    global result
    # N 행까지 퀸을 겹치지 않고 모두 놓은경우 최대로 놓을 수 있는 퀸을 다 놓은 경우
    if count == N:
        result += 1
        return

    for j in range(N):
        # 퀸이 놓여진 적이 없는경우
        if visited_1[j] == 0 and visited_2[count+j] == 0 and visited_3[count-j] == 0:
            # 퀸을 놓았다는 표시를 해주고
            visited_1[j] = 1
            visited_2[count + j] = 1
            visited_3[count - j] = 1

            # 퀸을 놓았으니 count + 1 해주고 다음 DFS 실시
            DFS(count + 1)

            # 가능한 모든 경우의 수를 구해야 하므로 위 DFS 가 끝났을 때 퀸 놓은 흔적 없애주기
            visited_1[j] = 0
            visited_2[count + j] = 0
            visited_3[count - j] = 0


N = int(input())
result = 0
# j값을 기준으로 위 쪽에 퀸이 있는지를 판별한 v1
visited_1 = [0] * N
# j 값을 기준으로 대각선 오른쪽에 퀸이 있는지를 판별한 v2
visited_2 = [0] * (2*N)
# j 값을 기준으로 대각선 왼쪽에 퀸이 있는지를 판별한 v3
visited_3 = [0] * (2*N)
DFS(0)
print(result)
