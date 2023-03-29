import sys
sys.stdin = open('input.txt')

string = list(input())
rev_string = string[::-1]

if string == rev_string:
    print(1)
else:
    print(0)