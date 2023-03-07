import sys
sudoku = [[0]*9 for _ in range(9)]
needed_rows = [[True for _ in range(9)] for _ in range(9)]  # 각 행에서 각각의 숫자에 대해 채워줄 필요가 있는가
needed_cols = [[True for _ in range(9)] for _ in range(9)]  # 각 열에서도
needed_boxes = [[[True for _ in range(9)] for _ in range(3)]for _ in range(3)]  # 각 상자에서도
needed = []  # 채워줄 필요가 있는 칸, 빈 칸
for r in range(9):
    for c, cell in enumerate(sys.stdin.readline().split()):
        if num := int(cell):  # 숫자가 있다면
            sudoku[r][c] = num  # 스도쿠를 채워줌
            num_idx = num - 1  # 인덱스는 0부터 시작하므로 -1
            needed_rows[r][num_idx] = False  # 각 행에서 해당 숫자는 채워줄 필요없음
            needed_cols[c][num_idx] = False  # 각 열에서도
            needed_boxes[r//3][c//3][num_idx] = False  # 각 상자에서도
        else:  # 숫자가 없다면
            needed.append((r, c)) # 빈 칸 리스트에 추가  

possible_num_idxs = [[] for _ in range(len(needed))] # 각각의 빈칸에 들어갈 수 있는 숫자들을 담은 리스트
for idx, coord in enumerate(needed):
    r, c = coord
    for num_idx in range(9):  # 각 숫자에 대해
        if needed_rows[r][num_idx] and needed_cols[c][num_idx] and needed_boxes[r//3][c//3][num_idx]:  # 빈 칸이 포함된 행, 열, 상자에서 해당 숫자가 없으면
            possible_num_idxs[idx].append(num_idx)  # 가능성 리스트에 추가

def backtrack(i):  # 빈 칸 리스트의 인덱스를 받아옴
    if i == len(needed):  # 모든 빈 칸을 채워줬으면 끝
        return True
    r, c = needed[i] 
    for num_idx in possible_num_idxs[i]:  # 각각의 가능성에 대해
        if needed_rows[r][num_idx] and needed_cols[c][num_idx] and needed_boxes[r//3][c//3][num_idx]:  # 유효하면
            sudoku[r][c] = num_idx + 1  # 스도쿠를 채워줌
            needed_rows[r][num_idx] = False  # 이제 각 행에서 해당 숫자는 채워줄 필요없음
            needed_cols[c][num_idx] = False  # 각 열에서도 
            needed_boxes[r//3][c//3][num_idx] = False  # 각 상자에서도
            if backtrack(i+1):  # 모든 빈 칸을 채워줬으면 끝
                return True
            sudoku[r][c] = 0  # 원상복구
            needed_rows[r][num_idx] = True  # 원상복구
            needed_cols[c][num_idx] = True  # 원상복구
            needed_boxes[r//3][c//3][num_idx] = True  # 원상복구
    return False

backtrack(0)
for row in sudoku:
    print(*row)
