'''
-> 문제요약
괗로 문자열이 있다.(괄호로만 구성된 문자열)
괄호 모양이 바르게 구성된 문자열은 vps라 한다.
입력으로 주어진 괄호 문자열이 vps인지 아닌지를 판단해서, 그 결과를 YES 아니면 NO로 나타내기

테스트 케이스는 T개로 각 줄마다 답을 출력하면 된다.

-> 아이디어
1. T만큼 반복해서 input을 입력 받고, 검토해서, 답을 출력한다.
2. 입력 하나를 받았을 때, 빈 스택을 하나 만든 다음 문자열을 for문으로 순회한다.
2-0. 문자열이 괄호가 아니라면 그냥 패스한다.
2-1. 문자열이 여는 괄호라면 일단 스택에 담는다.
2-2. 문자열이 닫는 괄호라면, 현재 스택의 top과 한 쌍을 이룰 것이라 가정하고, 한쌍을 날린다.(스택의 top을 삭제, 즉 pop한다는 뜻)
     이 때, 스택에 더 이상 괄호가 없다면 에러가 날 것이고 그렇다면 vps가 아닌 것.
3. 2번 과정이 문제없이 끝났을 때, 스택이 비어있다면 vps이고, 아니라면 vps가 아니다.
'''

def is_vps(inp_str):

    stack = []
    for i in inp_str:
        if i == '(':
            stack.append(i)
        elif i == ')':
            try:
                stack.pop()
            except:
                return False

    if stack:
        return False
    return True

T = int(input())

for t in range(T):  # 테스트 케이스만큼 반복
    x = input()

    if is_vps(x):
        print('YES')
    else:
        print('NO')

