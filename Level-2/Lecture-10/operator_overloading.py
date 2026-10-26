class Number: 
    def __init__(self,value): 
        if type(value) == int or type(value) == float: 
            self.value = value 
        else: 
            print("Cannot assign value. Please enter a int or float value")
            self.value = 0 
    def __str__(self):
        return str(self.value)

    def __add__(self,other): 
        result = self.value + other.value 
        return Number(result)

    def __sub__(self,other): 
        result = self.value - other.value 
        return Number(result)

    def __mul__(self,other): 
        result = self.value * other.value 
        return Number(result)

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
print(num1 // num2)

