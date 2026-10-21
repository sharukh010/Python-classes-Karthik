class CalculatorV0:
    def __init__(self): 
        self.num1 = 0 
        self.num2 = 0 
    def set_num1(self,num1): 
        self.num1 = num1 
    def set_num2(self,num2): 
        self.num2 = num2 
    def get_num1(self): 
        return self.num1 
    def get_num2(self): 
        return self.num2 
class CalculatorV1(CalculatorV0): 
    def __init__(self): 
        super().__init__()
    def set_nums(self,num1,num2): 
        self.num1 = num1 
        self.num2 = num2 
    def get_nums(self): 
        return (self.num1,self.num2)
    def add(self):
        return self.num1 + self.num2 
    def sub(self): 
        return self.num1 - self.num2 
    def multiply(self): 
        return self.num1 * self.num2 
    def division(self): 
        if self.num2 == 0: 
            print("Cannot divide with 0")
        else: 
            return self.num1 / self.num2 
        # 5/0 -> this not possible 
        # 0/5 - 0 -> this is possible 
cal1 = CalculatorV0()
# cal1.set_num1(10)
# cal1.set_num2(20)
# instead this it would great if we can set both the number at the same time 
# in version 1 we will add add,subtraction,division , multiplication 
cal2 = CalculatorV1()
cal2.set_nums(10,20)
print(cal2.add())
print(cal2.get_nums())