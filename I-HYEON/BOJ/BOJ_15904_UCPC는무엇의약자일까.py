'''
아이디어
1. 문자열을 받아와서 한문자씩 잘라 리스트에 담는다.
2. UCPC가 있는지 확인한다.
3. 통과하면 "I love UCPC", 통과못하면 "I hate UCPC"라고 출력한다.
'''

lst = list(input())
lst = list(filter(lambda x:x.isupper(),lst))
UCPC = 'UCPC'

ans = []
s,e = 0,0
while s < 4 and e<len(lst):
    if UCPC[s] != lst[e]:
        e += 1
        if e >= len(lst):
            break
    else:
        ans.append(UCPC[s])
        s += 1
        if s >= 4:
            break

answer = ''.join(ans)
if answer == 'UCPC':
    print('I love UCPC')
else:
    print('I hate UCPC')