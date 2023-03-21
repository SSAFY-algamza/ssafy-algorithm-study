N = int(input())
for num in range(N):
    stack = []
    a=input()
    for i in a:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if stack:
                stack.pop()
            # 스택에 괄호가 없는데 닫는괄호가 올 경우
            else:
                print('NO')
                break # 더 조사할 필요 없으므로 break
    # break문에 걸리지 않고 반복문이 종료 되었을때
    else:
        # 정상 종료되어 스택이 비어있는 경우
        if not stack:
            print('YES')
        # 정상 종료해도 여는 괄호가 남아 있는 경우
        else:
            print('NO')