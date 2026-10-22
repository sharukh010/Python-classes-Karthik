class GrandParent: 
    def __init__(self): 
        self.property1 = "Farm House"
        self.property2 = "5 star Hotel"

class Parent(GrandParent): 
    def __init__(self):
        super().__init__()  
        self.property3 = "Casino"
        self.property4 = "Swimming Pool"

class Child(Parent): 
    def __init__(self): 
        super().__init__()
        self.property5 = "House"

child = Child()
print(child.property1)
print(child.property3)
print(child.property5)