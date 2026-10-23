class Parent1:
    def __init__(self): 
        self.property1 = "house"
        self.property2 = "casino"

class Parent2: 
    def __init__(self): 
        self.property3 = "horses"
        self.property4 = "farms" 

class Child1(Parent1): 
    def __init__(self): 
        self.child_number = 1 

class Child2(Parent1,Parent2): # heirarchy + multiple inheritence 
    def __init__(self): 
        self.child_number = 2 