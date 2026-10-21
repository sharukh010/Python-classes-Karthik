class Parent: 
    def __init__(self,first_name,last_name): 
        self.first_name = first_name
        self.last_name = last_name 

    def display(self): 
        print(f"{self.first_name} {self.last_name}")

class Child(Parent): # this is how you perform inheritence 
    # now child class can access all the properties and methods from parent class 
    def __init__(self,first_name,last_name,school_name): 
        super().__init__(first_name,last_name) # while creating child we are also creating a parent 
        self.school = school_name 

    def get_school(self): 
        return self.school 

parent = Parent("Ben","Parker")
child = Child("Peter","Parker","New York state high school")
# parent.display()
# parent.get_school() # this will give error because get_school is not in parent class 
# child.display() this will work 
print(child.get_school())