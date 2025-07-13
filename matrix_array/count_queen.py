def find_max(arr, current_max_val=0, current_idx=0, max_idx=0):
    if len(arr) == 0:
        return [max_idx, current_max_val]

    if current_max_val < arr[0]:
        current_max_val = arr[0]
        max_idx = current_idx

    arr.pop(0)
    current_idx += 1
    return find_max(arr, current_max_val, current_idx, max_idx)


col_row_amount = int(input())

matrix = []
rev_matrix = [[] for c in range(col_row_amount)]

for i in range(col_row_amount):
    row = list(map(int, input().split()))
    for j in range(col_row_amount):
        rev_matrix[j].append(row[j])
    matrix.append(row)


max_row_idx = []
for i in range(len(matrix)):
    row = matrix[i].copy()
    max_row_val = find_max(row)
    max_row_idx.append([i] + max_row_val)

max_col_idx = []
for i in range(len(max_row_idx)):
    checking_max_row = max_row_idx[i].copy()
    col = rev_matrix[checking_max_row[1]].copy()
    max_col_val = find_max(col)
    if checking_max_row[2] == max_col_val[1]:
        max_col_idx.append(checking_max_row)

max_cross_idx = []
for i in range(len(max_col_idx)):
    checking_max_col = max_col_idx[i].copy()
    cross_arr = [checking_max_col[2]]
    # up
    for j in range(checking_max_col[0] - 1, -1, -1):
        step = checking_max_col[0] - j
        left = [j, checking_max_col[1] - step]
        right = [j, checking_max_col[1] + step]
        if left[1] >= 0:
            cross_arr.append(matrix[left[0]][left[1]])
        if right[1] < col_row_amount:
            cross_arr.append(matrix[right[0]][right[1]])
    # down
    for j in range(checking_max_col[0] + 1, col_row_amount):
        step = j - checking_max_col[0]
        left = [j, checking_max_col[1] - step]
        right = [j, checking_max_col[1] + step]
        if left[1] >= 0:
            cross_arr.append(matrix[left[0]][left[1]])
        if right[1] < col_row_amount:
            cross_arr.append(matrix[right[0]][right[1]])
    max_cross_val = find_max(cross_arr)
    if checking_max_col[2] == max_cross_val[1]:
        max_cross_idx.append(checking_max_col)
        
print(len(max_cross_idx))
