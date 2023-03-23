import sys
N = int(sys.stdin.readline())
nums1 = [int(i) for i in sys.stdin.readline().split()]

if N == 1:
    print(sum(nums1)-max(nums1))
else:
    nums2 = []
    nums3 = []
    for i in range(6):
        for j in range(i+1, 6):
            if i != 5-j:
                nums2.append(nums1[i]+nums1[j])
    for i in (0, 5):
        for j in (1, 4):
            for k in (2, 3):
                nums3.append(nums1[i]+nums1[j]+nums1[k])
    side1 = min(nums1)*(((N-2)**2)*5 + (N-2)*4)
    side2 = min(nums2)*((N-2)*8 + 4)
    side3 = min(nums3)*4
    print(side1+side2+side3)
