import sys
sys.stdin = open('input.txt')

n, m = map(int, input().split())

listen = set()
for i in range(n):
    listen.add(input())

see = set()
for i in range(m):
    see.add(input())

result = sorted(list(listen & see))

print(len(result))
for i in result:
    print(i)


