nums = [[1,2,3,10],
        [4,5,6,11],
        [7,8,9,12]]
#        0   1   2 
# row index 
# all the elements in outer list are considered as rows 
# all the elements inside the inner list are considered as cols 
# list_name[row_index][col_index]
# print(nums[2][1])
# print(len(nums))# 3  number of rows 
# print(len(nums[0]))#4  number of columns 
columns = len(nums[0])
rows = len(nums)

for r in range(rows): 
    for c in range(columns): 
        print(nums[r][c])