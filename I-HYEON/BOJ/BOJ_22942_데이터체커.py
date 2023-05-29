'''
-> 문제설명
여러개의 원이 주어지고, 그 중 임의의 원 두개를 선택했을 때 모든 케이스에서 교점이 존재하지 않으면
YES, 아니면 NO를 출력해야하는 문제

-> 아이디어
1. for문으로 입력정보를 받아오는데 (x축과의 교점,몇번째원인지,왼쪽교점인지오른쪽교점인지) 튜플로 넣는다.
2. 그렇게 만든 리스트를 sort로 정렬시킨다.
3. 빈스택 하나와, 셋 하나를 만들어둔 후, 2번에서 만든 리스트를 순회하며 검토한다.
3-1. 튜플을 하나씩 가져와서, 왼쪽교점의 경우 스택에 추가하고, 오른쪽 교점의 경우 셋에 추가하고, 스택에서 하나를 제거한다.
3-2. 만약 어떤 튜플이 이미 셋에 있다면, 조건에 부합하지 않으므로 print(NO)하고 끝낸다.
3-3. 만약 어떤 튜플이 오른쪽 교점임에도 짝이 맞지 않는 원이라면 print(NO)하고 끝낸다.
'''
import sys
input = sys.stdin.readline

N = int(input())

lst = []
for i in range(N):
    a, b = map(int,input().split())
    lst.append((a-b,i,0))
    lst.append((a+b,i,1))

lst.sort()
stack = []
reduple_check=set()
for x,y,z in lst:
    if x in reduple_check:
        print('NO')
        break
    if z == 0:
        stack.append((x,y))
    elif y != stack[-1][1]:
        print('NO')
        break
    else:
        reduple_check.add(x)
        stack.pop()
else:
    print('YES')