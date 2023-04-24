'''
1.이차원 배열을 반복문을 돌려 하나씩(리스트 한개) 가져온다.
2. 이 때 가져온 리스트와 같은 크기의 배열(모두 0으로 초기화)을 만들어 dp라는 이름에 할당.
3.그리고 반복문을 하나 더 돌린다.
가져온 리스트 원소를 순회하는데, 순회하면서 dp배열의 해당 인덱스(j) 원소 값을 갱신한다.
how? 가져온 리스트 보다 앞전 리스트의 j-1,j 인덱스 값 중 더 큰 쪽의 값과 현재 원소를 더한 값으로 갱신 한다.
4. 다음 리스트로 가기 전에 현재 리스트를 dp 배열로 바꿔치기 한다.(저장된 값으로 다음리스트 때 이용해야하니까)
3. 이 방식으로 가면 특정 숫자의 왼쪽 위 숫자, 오른쪽 위 숫자 에 저장된 최대 합 중 더 큰 수로 본인이 계속 갱신된다.
4. 최종적으로 마지막 리스트에도 같은 행위를 반복하고, 마지막 리스트 값 중 가장 큰 값을 프린트 한다.
'''


N = int(input())
lists = [list(map(int,input().split())) for _ in range(N)]

for i in range(1, N):
    DP = [0]*len(lists[i])
    for j in range(len(lists[i])):
        if j-1 >= 0:
            DP[j] = max(DP[j], lists[i-1][j-1]+lists[i][j])
        if j < len(lists[i-1]):
            DP[j] = max(DP[j], lists[i-1][j]+lists[i][j])
    lists[i] = DP

print(max(lists[N-1]))