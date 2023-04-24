number = input()
mydict = {x: 0 for x in range(0, 10)}


if len(number) == 0:
    print(0)
else:
    for i in number:
        mydict[int(i)] += 1

    if abs(mydict[6] - mydict[9]) >= 2:
        mydict[6] = min(mydict[6], mydict[9]) + abs(mydict[6] - mydict[9])//2 + abs(mydict[6] - mydict[9])%2
        mydict[9] = mydict[6]

    print(max(mydict.values()))
'''
숫자를 키로 개수를 값으로 딕셔너리를 만든다.
딕셔너리의 값들 중 가장 큰 숫자를 출력하면 필요한 세트의 개수를 알 수 있다.

단, 6과 9 의 경우는 예외 처리를 해줘야함.
한 세트에 6과 9가 있으므로 6이 두번 카운트 되어도 세트 하나로 해결할 수 있다.
9도 마찬가지로 두번 카운트 되어도 세트 하나로 해결 할 수 있다.
즉, 6과 9의 차이가 두 개 이상일 때는, 그 차이를 2로 나눈값을 실제 카운트로 세어야한다는 뜻.
'''