'''
비밀번호를 구해야 함
사용자가 누른 명령을 모두 기록한다.
키보드로 입력한 키는 알파벳 대문자, 소문자, 숫자, 백스페이스, 화살표 만 입력함
비밀번호로 올 수 있는 건 알파벳 대문자, 소문자, 숫자 3가지만 올 수 있음

조건
1. 백스페이스 - 가 입력되면 커서 바로앞의 글자가 존재할 때 그 글자를 지운다 >> stack.pop()
2. 화살표 < 와 > 커서의 위치 변경

구현
기본적으로 문자들을 stack에 append 해줌
> 화살표 입력시 stack 위치 변경
< 화살표 입력시 stack 위치 변경
stack의 위치변경을 위해서 stack을 2개로 나누기
'''
import sys
T = int(input())
for tc in range(T):
    stack = []
    another_stack = []
    password = sys.stdin.readline().strip()
    for word in password:
        # 기본적으로 문자를 추가해주는 stack에서 pop
        if word == '-':
            if stack:
                stack.pop()
        # 기존 stack에서 위치변경
        elif word == '<':
            if stack:
                another_stack.append(stack.pop())
        # 반대의 경우
        elif word == '>':
            if another_stack:
                stack.append(another_stack.pop())
        # 이외의 문자 stack 에 추가해주기
        else:
            stack.append(word)
    # 1. stack 출력해보니 테케가 맞아서 그냥 stack만 언패킹 해서 공백제거로 제출 > 틀림
    # print(stack)
    # print(another_stack)
    # print(*stack, sep='')

    # 2. another_stack에도 정답이 남아 있을 수 도 있겠다 싶어서
    # 두개의 리스트를 더해서 언패킹으로 출력해봄 > 틀림
    # result = stack + another_stack
    # print(*result, sep='')

    # 3. another_stack 으로 넘어가는 과정에서 순서가 뒤집어 졌나 싶어서 거꾸로 뒤집어서 더해봄
    # 기존 스택만 출력했을 때는 결과가 제대로 나왔어서 another_stack만 뒤집어봄
    another_stack = another_stack[::-1]
    result = stack + another_stack
    print(*result, sep='')
