matrix = [[1,2,3],[4,5,6]]
new_matrix=[]
mat_rows=len(matrix)
mat_columns=len(matrix[0])

print(f'rows:{mat_rows},columns:{mat_columns}')

for col in range(0,mat_columns):
     new_matrix.append([matrix[r][col] for r in range(0,mat_rows)])
     
print(new_matrix)