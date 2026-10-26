class Number: 
    def __init__(self,value): 
        if isinstance(value,(int,float)): 
            self.value = value 
        else: 
            print("Cannot assign value. Please enter a int or float value")
            self.value = 0 
    def __str__(self):
        return str(self.value)

    def __add__(self,other): 
        if isinstance(other,(int,float)): 
            return Number(self.value + other)
        elif isinstance(other,Number): 
            result = self.value + other.value 
            return Number(result)
        else:
            print(f"+ is not supported between {type(self)} and {type(other)}")

    def __sub__(self,other): 
        if isinstance(other,(int,float)): 
            return Number(self.value - other)
        elif isinstance(other,Number): 
            result = self.value - other.value 
            return Number(result)
        else: 
            print(f"- is not supported between {type(self)} and {type(other)}")

    def __mul__(self,other): 
        if isinstance(other,(int,float)): 
            return Number(self.value * other)
        elif isinstance(other,Number): 
            result = self.value * other.value 
            return Number(result)
        else: 
            print(f"* is not supported between {type(self)} and {type(other)}")

    def __truediv__(self,other): 
        result = self.value / other.value 
        return Number(result)

    def __pow__(self,other): 
        result = self.value ** other.value 
        return Number(result)

    def __mod__(self,other): 
        result = self.value % other.value 
        return Number(result)

    def __floordiv__(self, other):
        result = self.value // other.value 
        return Number(result)

    # comparision operators 
    def __eq__(self,other): 
        return self.value == other.value 

    def __ne__(self,other): 
        return self.value != other.value 

    def __lt__(self,other): 
        return self.value < other.value 

    def __gt__(self,other): 
        return self.value > other.value 

    def __le__(self,other): # less than or equal to 
        return self.value <= other.value 

    def __ge__(self,other): 
        return self.value >= other.value 


num1 = Number(10)
num2 = Number(2)
# print(num1)
# print(num2)
# print(num1 + num2)
# print(num1 - num2) # this is allowed 
# print(num1 * num2)
# print(num1 / num2)
# print(num1 ** num2)
# print(num1 % num2)
# print(num1 // num2)
# print(num1 == num2)# 10 == 2 : False
# print(num1 != num2)# 10 != 2 : True 
# print(num1 < num2)# 10 < 2 : False 
# print(num1 > num2)# 10 > 2 : True 
# print(num1 <= num2)# 10 <= 2: False 
# print(num1 >= num2)# 10 >= 2: True 

print(num1 + 3.5)

