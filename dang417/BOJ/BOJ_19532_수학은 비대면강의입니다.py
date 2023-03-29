import sys
sys.stdin = open('input.txt')

a, b, c, d, e, f = map(int, input().split())

y = ((a*f)-(c*d))//((a*e)-(b*d))

if a == 0:
    x = (f-e*y)//d
else:
    x = (c-b*y)//a

print(x, y)