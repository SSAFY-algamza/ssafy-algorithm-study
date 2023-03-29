from collections import deque
T = int(input())

for _ in range(T):
    keylogger = input()
    password = deque([])
    temp_password = deque([])

    for k in keylogger:
        if k.isalnum():
            password.append(k)
        elif k == "<" and password:
            temp_password.appendleft(password.pop())
        elif k == ">" and temp_password:
            password.append(temp_password.popleft())
        elif k == "-" and password:
            password.pop()

    print(''.join(password)+''.join(temp_password))