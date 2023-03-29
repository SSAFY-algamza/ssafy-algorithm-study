import sys

N = int(sys.stdin.readline())
init = [int(i) for i in sys.stdin.readline().rstrip()]
target = [int(i) for i in sys.stdin.readline().rstrip()]

for first_switch in (False, True):
    cnt = 0
    init_copy = init[:]

    if first_switch:
        cnt += 1
        init_copy[0] = 1 - init_copy[0]
        init_copy[1] = 1 - init_copy[1]

    for idx in range(1, N):
        if init_copy[idx - 1] != target[idx - 1]:
            cnt += 1
            init_copy[idx - 1] = 1 - init_copy[idx - 1]
            init_copy[idx] = 1 - init_copy[idx]
            if idx + 1 < N:
                init_copy[idx + 1] = 1 - init_copy[idx + 1]

    if init_copy == target:
        print(cnt)
        break

else:
    print(-1)
