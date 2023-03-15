import sys
N = int(sys.stdin.readline())
coords_list = [int(i) for i in sys.stdin.readline().split()]
coords_dict = {coord: cnt for cnt,
               coord in enumerate(sorted(list(set(coords_list))))}
for coord in coords_list:
    print(coords_dict[coord], end=" ")
