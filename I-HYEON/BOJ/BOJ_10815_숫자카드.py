'''
상근이가 가진 숫자카드가 n개
그리고 주어지는 숫자 m개
이 숫자들을 하나씩 가져와서 숫자가 숫자카드에 있으면 1없으면 0을 출력하는 프로그램을 작성하라

이분탐색을 해서 있으면 true, 없으면 false를 반환하는 함수를 만들고
숫자를 하나씩 받아와서 함수에 돌려서 출력하기
'''
N = int(input())
cards = list(map(int,input().split()))
cards.sort()
M = int(input())
numbers = list(map(int,input().split()))

def findNum(num):
    s, e = 0, N-1  # 시작점은 인덱스0, 종료점은 인덱스 N-1
    while s <= e:  # 서로 떨어져있는 동안은 계속 반복
        mid = (s+e)//2  # mid 설정
        if num < cards[mid]:  # mid값이 더 크면 종료점을 옮기고
            e = mid-1
        elif num > cards[mid]:  # mid값이 더 작으면 시작점을 옮기고
            s = mid+1
        else:  # 같으면 찾은 것이므로 True를 리턴한다.
            return True
    return False

for i in range(M):
    if findNum(numbers[i]):
        print(1,end=" ")
    else:
        print(0,end=" ")