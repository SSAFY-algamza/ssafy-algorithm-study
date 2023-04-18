import sys
input = sys.stdin.readline

V, E = map(int,input().split())  # 정점의 개수와 간선의 개수를 입력

# 연결요소 중 가장 작은 값을 저장할 배열을 하나 생성한다. 처음에는 자기 자신을 저장한다.
Vroot = [i for i in range(V+1)]

# 연결정보와 가중치가 담긴 정보(입력값)를 리스트로 담아온다음, 가중치 기준으로 정렬한다.
E_list = []
for _ in range(E):
    E_list.append(list(map(int,input().split())))

E_list.sort(key=lambda x: x[2])

def find(x):
    if x != Vroot[x]:
        Vroot[x] = find(Vroot[x])
    return Vroot[x]

answer = 0  # 답을 0으로 초기화하고 시작
for s, e, w in E_list:
    sRoot = find(s)  # s의 최상위 루트 노드를 sRoot에 할당
    eRoot = find(e)  # e의 최상위 루트 노드를 eRoot에 할당
    if sRoot != eRoot:  #  둘이 같지 않을 때 s와 e를 같은 집합에 속하도록 합침.
        '''
        만약 둘이 같은 집합에 속해 있다면, 해당 간선을 선택하면 사이클이 형성되기 때문에 무시해야한다
        그래서 둘이 같지 않을 때만, 여기로 들어와서 어느쪽이 큰지를 따진다.
        더 작은 숫자로 바꿔준다
        '''
        if sRoot > eRoot:
            Vroot[sRoot] = eRoot
        else:
            Vroot[eRoot] = sRoot
        answer += w

print(answer)