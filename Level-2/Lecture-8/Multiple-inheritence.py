class Father: 
    def __init__(self): 
        self.property1 = "drawing artist"
        self.property2 = "mathematical skills"

    def calculate(self,num1,operator,num2): 
        match operator: 
            case "+": 
                return num1 + num2 
            case "-": 
                return num1 - num2 
            case "x": 
                return num1 * num2 
            case "/": 
                return num1 / num2 
            case _ :
                print(f"Invalid operator {operator}. we only support + , - , x , / .") 
                return None 
class Mother: 
    def __init__(self):
        self.property3 = "dancing skills"
        self.property4 = "cooking skills"
    def cooking(self,dish): 
        print(f"Cooking {dish}...")

class Child(Father,Mother):
    def __init__(self): 
        Father.__init__(self)
        Mother.__init__(self)
        self.property5 = "football skills"
        self.property6 = "Speak in French"
    def speak_in_frech(self): 
        print("Bonjur")

child = Child()
print(child.property1)
print(child.property3)
print(child.calculate(10,"+",20))
child.cooking("Biriyani")
child.speak_in_frech()

