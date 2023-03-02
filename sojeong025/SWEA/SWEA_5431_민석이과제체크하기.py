'''
수강생들은 1번에서 N번 까지 번호가 매겨져 있고,
어떤 번호의 사람이 제출했는지에 대한 목록 받음
과제를 제출하지 않은 사람의 번호를 오름차순으로 출력하는 프로그램
'''
import sys
sys.stdin = open('5431_input.txt')

T = int(input())
for tc in range(1, T+1):
    # N 수강생 수 / K 과제 제출한 사람의 수
    N, K = map(int, input().split())
    number = list(map(int, input().split()))

    # 제출 안한 사람의 번호를 담을 리스트
    answer = []
    # 1부터 N까지 수강생 번호 중에
    for i in range(1, N+1):
        # 제출한 사람의 번호가 없으면 리스트에 append
        if i not in number:
            answer.append(i)

    # 오름차순으로 출력 (리스트 언패킹)
    print(f'#{tc}', *sorted(answer))

    # 내림차순으로 출력한다면,
    # print(f'#{tc}', *sorted(answer, reverse=True))

