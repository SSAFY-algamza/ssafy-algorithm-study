N = int(input())

if (N%5)%2: #나머지가 2로나누어지지 않으면
    if N == 1 or N == 3:
        ans = -1
    else:
        five_ones = N//5-1
        two_ones = (N - 5*five_ones)//2
        ans = five_ones+two_ones
else:
    ans = N//5 + (N%5)//2

print(ans)