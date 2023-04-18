N = int(input())
numbers = list(map(int, input().split()))  # 연산에 사용할 숫자 배열
p, s, m, d = map(int, input().split())  # 순서대로 +,-,*,// 의 개수

minimum = 1e9  # 최소값을 -10 억으로 초기화
maximum = -1e9  # 최대값을 10 억으로 초기화


def DFS(depth, result, plus, sub, mul, div):  # DFS 로 연산하는 함수
    global minimum, maximum

    if depth == N -1 :  # 깊이가 N-1이 되면 (연산자 개수만큼 다 사용하면) 재귀 중단

        minimum = min(minimum, result)
        maximum = max(maximum, result)
        return

    else:  # 사용하지 않은 연산자가 있으면 해당 연산을 수행하고 재귀 호출
        if plus != 0:
            DFS(depth+1, result + numbers[depth+1], plus-1, sub, mul, div)
        if sub != 0:
            DFS(depth+1, result - numbers[depth+1], plus, sub-1, mul, div)
        if mul != 0:
            DFS(depth+1, result * numbers[depth + 1], plus, sub, mul-1, div)
        if div != 0:
            DFS(depth+1, int(result / numbers[depth + 1]), plus, sub, mul, div-1)  # // 사용하면 예제 3 통과 못함.

DFS(0,numbers[0], p, s, m, d)

print(maximum)
print(minimum)

'''
a = -3 // 2 ( // 연산자는 나눈 뒤 소수점 이하 자리를 '버림'함. 즉, 본인보다 더 작은 수 중 가장 큰 정수를 반환)
b = -3 / 2  (/ 연산자는 그냥 나눔. 따라서 음수 연산에서 /로 연산하고 int형으로 변환하는 것이 문제 조건에 적합)
print(a)         -2 ->    -1.5를 버림한 것이므로 -2이 된다.
print(int(b))    1  ->    -1.5 의 정수 부분만을 반환하는 것이므로 -1 이 된다.
'''