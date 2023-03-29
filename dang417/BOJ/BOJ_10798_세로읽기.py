import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

str_arr = [[''] * 15 for _ in range(5)]

for i in range(5):
    string = input().rstrip()
    for j in range(len(string)):
        str_arr[i][j] = string[j]

for j in range(15):
    for i in range(5):
        print(str_arr[i][j], end = '')