matrix_a = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
matrix_b = [[5,4,1],[2,6,3],[9,7,8],[12,11,10]]
# matrix_c = [[0,0,0],[0,0,0],[0,0,0]]
# matrix_c = [] -> matrix_c[0][0] this will give you error 
rows = len(matrix_a)
cols = len(matrix_a[0])
matrix_c = [[0 for c in range(cols)]for r in range(rows)]
# print(matrix_c)
# for r in range(rows): 
#     for c in range(cols): 
#         matrix_c[r][c] = matrix_a[r][c] + matrix_b[r][c]
for r in range(rows): 
    for c in range(cols): 
        matrix_c[r][c] = matrix_a[r][c] - matrix_b[r][c]


print(matrix_c)