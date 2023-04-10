text = input().replace("()", "R")
stack = []
cnt = 0
for char in text:
    if char == "(":
        stack.append(char)
        cnt += 1
    elif stack and stack[-1] == "(" and char == ")":
        stack.pop()
    elif char == "R":
        cnt += len(stack)
print(cnt)