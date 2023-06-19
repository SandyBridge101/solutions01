matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 16
mat_rows=len(matrix)
mat_cols=len(matrix[0])

for r in range(0,mat_rows):
    if target>=matrix[r][0] and target<=matrix[r][mat_cols-1]:
        print(target in matrix[r])