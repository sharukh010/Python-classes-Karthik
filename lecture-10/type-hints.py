# type hints will let the user 
# understand what data does our function need 
# and what data it returns
# this will make programming easy 
import random 
import math
# def add(num1,num2): 
#     return num1 + num2 
def add(num1: float,num2: float)->float:
    """
    - It takes two numbers as input and return the sum
    ### Args:
    - num1 (float) : first number 
    - num2 (float) : second number 
    ### Returns: 
    - float : num1 + num2
    """ 
    return num1 + num2 
# def display(nums: list[float]): 
#     print(nums)
#     return 
# add()
# display()
# input()
# random.randint()
# random.binomialvariate()
add()

def square_area(length: float) ->float:
    """
    - It calculates the area of square. 
    ### Args: 
    - length (float) : length of the side of a square 
    ### Returns: 
    - float : area of the square
    """
    return length ** 2
def circle_area(radius: float) ->float: # signature of the function 
    """
    It calculates the area of circle. 
    ### Args: 
    - radius (float) : radius of the circle
    ### Returns: 
    - float: area of square 
    """
    return math.pi * radius ** 2
def rectangle_area(length: float,breadth: float) ->float:
    """
    It calculates the area of rectangle. 
    ### Args: 
    - length (float): length of the rectangle 
    - breadth (float): breadth of the rectangle 
    ### Returns: 
    - float: area of a rectangle 
    """
    return length * breadth

def display(first_name: str ,last_name : str | None ):
    print(f"First Name: {first_name}")
    if last_name != None: 
        print(f"Last Name: {last_name}") 
display("Karthik",None)