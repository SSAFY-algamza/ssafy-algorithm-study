N = input()
cnts = [0]*10
for i in N:
    cnts[int(i)] += 1
six_nine = cnts[6]+cnts[9]
cnts[6] = cnts[9] = six_nine//2 + six_nine%2
print(max(cnts))
