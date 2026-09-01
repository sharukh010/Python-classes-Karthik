# value = print()
# print(f"value: {value}")
# num1,num2 are arguments 
def add(num1,num2): 
    result = 0
    result = num1 + num2 
    # print(id(result))
    return result 
# 10,20 are parameters 
result = add(10,20) # positional parameters 
# print(f"result = {result}")
# print(id(result))

"""
Exercise: 
write functions for 
sub(num1,num2)- return you subtraction 
mul(num1,num2) - return multiplication 
div(num1,num2) - return division 
- if num2 is equal to 0 you should print 
division is not possible 
power(num1,num2) - num1^num2 
"""