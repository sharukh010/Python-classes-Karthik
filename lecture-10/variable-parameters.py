def add(*nums)->float: 
    # print(nums)
    result = 0 
    for num in nums:
        result += num 
    return result 
# def add(num1: float,num2: float,*nums): 
#     result = num1 + num2 
#     for num in nums: 
#         result += num 
# #     return result 
# print(add(1,2))
# print(add(1,2,3,4))
nums = [1,2,3,4]
print(add(*nums))
# *nums will unpack the list and pass each value as a seperate parameter 
# print(add(1,2,3,4))