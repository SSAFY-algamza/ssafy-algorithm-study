N = int(input())
numbers = [i for i in range(1, N+1)]
drop_number= []

while len(numbers) != 1:
    drop_number.append(numbers.pop(0))
    numbers.append(numbers.pop(0))

for i in drop_number:
    print(i, end= ' ')
print(numbers[0])