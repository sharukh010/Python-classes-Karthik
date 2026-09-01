# Two ways you can pass parameters:
# 1. positional: the values you pass will store in the sequence 
"""
ex: display(first_name,last_name) 
display("john","doe") 
"john" -> first_name 
"doe" -> last_name 
"""
#2. keyword: the values are assigned while calling the function 
"""
display(last_name="doe",first_name="john")
"""
def display(first_name,last_name): 
    print(first_name,last_name)

# display("john","doe")
# display("doe","john")
# display(last_name="doe",first_name="john")
# display("john","c","doe") # gives error 
# display() # gives error 

def get_min_max(num1,num2): 
    min_ = num1 if num1 < num2 else num2 
    max_ = num1 if num1 > num2 else num2 
    return min_,max_

min_,max_ = get_min_max(5,4)
print(f"Minimum = {min_}")
print(f"Maximum = {max_}")