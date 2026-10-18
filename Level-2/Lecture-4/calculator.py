class Calculator: 
    def __init__(self): 
        # you will define you're properites 
        # Calculator you can assume it as noun 
        # self you can assume it as pronoun for Calculator 
        # inside Calculator whenever you say self you're taking about 
        # the Calculator 
        # self is reference to the current object 
        self.num1 = 0 
        self.num2 = 0 
        # num1 and num2 -> are object variables 
        # name -> is not an object variable 

    def add(self): 
        return self.num1 + self.num2 
    def sub(self): 
        return self.num1 - self.num2 
    def mul(self): 
        return self.num1 * self.num2 
    def div(self): 
        return self.num1 / self.num2 

    
cal1 = Calculator() # this is how you create an object 
cal2 = Calculator() 
cal2.num1 = 30 
cal2.num2 = 40 
cal1.num1 = 10 
cal1.num2 = 20 
# print(cal1.num1)
# print(cal1.num2)
# print(cal2.num1)
# print(cal2.num2)
# any changes you make to one object will not effect the other object 
print("Result of cal1: ")
print(cal1.add())
print(cal1.sub())
print(cal1.mul())
print(cal1.div())
print("Result of cal2: ")
print(cal2.add())
print(cal2.sub())
print(cal2.mul())
print(cal2.div())