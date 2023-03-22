import sys
M = int(sys.stdin.readline())
S = set()
for _ in range(M):
    command = sys.stdin.readline().split()
    operator = command[0]
    if operator == "all":
        S = set([i for i in range(1, 21)])
        continue

    if operator == "empty":
        S = set()
        continue

    num = int(command[1])
    if operator == "add":
        S.add(num)
        continue

    if operator == "remove":
        S -= {num}
        continue

    if operator == "check":
        print(1 if num in S else 0)
        continue

    if operator == "toggle":
        if num in S:
            S -= {num}
            continue
        S.add(num)
