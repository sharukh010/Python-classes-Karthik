matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [10,11,12]
]
# print(matrix)
# in 2D list you have two index (row,col) this indexes starts from 0 
# print(matrix[1][1])
# print(matrix[2][2])
# for row in matrix: 
#     for col in row: 
#         print(col)
print(f"Rows: {len(matrix)}")
print(f"Cols: {len(matrix[0])}")
for row in range(len(matrix)): 
    for col in range(len(matrix[0])): 
        print(matrix[row][col])