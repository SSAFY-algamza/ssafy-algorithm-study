N, M = map(int, input().split())
# N = 듣도 못한 사람
# M = 보도 못한 사람

N_list = set(input() for i in range(N))
M_list = set(input() for i in range(M))

total_list = list(N_list & M_list)
total_list.sort()

print(len(total_list))
for i in total_list:
    print(i)

'''
문제
듣도 못한 사람 N 이 주어짐
보도 못한 사람 M이 주어짐
듣도 보도 못한 사람의 수와 이름을 사전순으로 출력하시오
--------------------------------------------------------------------------------------------------------------------------------------------------
처음 접근법 => N, M 입력 받은뒤 
N_list와 M_list 만들어서
입력값을 리스트에 append하는 형식으로 만듦
이후 두번의 반복문을 돌며 값이 같을 경우 total_list에 넣어줌
사전순으로 출력하기 위해 total_list를 sort로 정렬 후 다시한번 반복문을 돌며 결과값을 출력
근데 런타임 에러(name) 발생
--------------------------------------------------------------------------------------------------------------------------------------------------
질문게시판 글 중 나와 비슷한 코드를 작성했는데 시간초과가 뜬다는 사람이 있다고 함
또 제약조건에 N, M이 자연수 500,000 이하라고 작성된걸 보고
최대 테스트케이스가 100만 이라 생각해서 반복문의 길이가 길어 런타임 에러가 뜬다 생각해서 시간을 줄일 방법을 생각해봄
리스트에 입력받은 값을 비교 하여 total_list에 넣어줘야 하기 때문에 비교연산자중 하나라고 처음에는 생각함
근데 반복문을 다시 두번 돌려야 하는데 i가 50만번 돌고 j도 50만번을 돌아야 하기 때문에 이중 for문은 안됨
다른방법이 교집합을 찾기 였음
비트 연산자 & 을 사용하면 두 집합의 교집합을 리스트 값으로 만들어서 넣어주는게 가능
문제는 리스트로 입력받은 값을 비트연산자로 비교하니 타입에러 발생, list와 list는 비교가 불가능
그래서 map 함수를 이용하여 str값으로 묶어주고 반환결과를 따로 지정안해서 map object로 받으면 되겠다라고 생각해서
N_list = (map(str, input()) for i in range(N))
M_list = (map(str, input()) for i in range(M))
이런식으로 코드를 작성함
그래도 결과값에 generator and genaretor 는 비교가 안된다 라고 나옴

명단에 중복이 없다 라고 해서 비교가 안되는게 명단에 중복 제거를 안해줘서 라고 생각하고
set()함수를 이용하여 중복을 제거함
이후 비트연산자 &을 이용하여 교집합을 구한뒤 정렬하여 출력하니 제대로된 결과값이 나옴

'''