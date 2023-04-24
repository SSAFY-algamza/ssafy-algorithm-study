zero = 0
one = 0
prev = None
for c in input():
    if prev != c:
        prev = c
        if c == "0":
            zero += 1
        else:
            one += 1
            
print(min(zero, one))