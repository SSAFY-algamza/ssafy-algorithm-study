quacks = input()
word = ['q', 'u', 'a', 'c', 'k']
visited = [False] * len(quacks)

cnt, idx = 0, 0
if len(quacks) % 5 != 0:
    print(-1)
else:
    for i in range(len(quacks)):  # 입력 문자열을 전체 순회
        if quacks[i] == 'q' and not visited[i]:  # 만약 해당 문자가 q 라면 아래의 검토 로직으로 빠짐

            cycle = True # quack 이라는 단어를 한싸이클 돌았는지 체크할 때 쓸 flag
            for j in range(len(quacks)):  # 입력 문자열 한 단어마다 다시 입력 문자열을 순회
                if word[idx] == quacks[j] and not visited[j]:  # 일치하는지 체크해서
                    visited[j] = True  # 사용해준다. 즉, 방문 체크해준다
                    if quacks[j] == 'k':  # k라는 문자가 등장하면 한 싸이클을 돈건지 체크
                        if cycle:  # 한 싸이클 돈 거 맞으면 개수 제대로 카운트 해주고
                            cnt += 1
                            cycle = False
                        idx = 0  # 아니면 그냥 idx 초기화 시키고 넘어가준다
                        continue
                    idx += 1  # 다음 for 문으로 갈 때 idx 증가시켜주기

    if cnt == 0 or not all(visited):
        print(-1)
    else:
        print(cnt)