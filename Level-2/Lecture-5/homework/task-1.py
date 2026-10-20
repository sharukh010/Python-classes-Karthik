"""A school stores one record for every student. Create a Student class with a default constructor.
A new student starts with roll_number 0, name "unnamed", marks 0 and grade "N/A". Add a
display method that prints the four lines shown in the sample output.
In your main program, create a student and display it. Then print a line of 20 dashes, set the roll
number, name, marks and grade to the values below, and display the student again.
Sample Input (values assigned after creation):
roll_number = 21
name = "Meera"
marks = 88
grade = "A"
Sample Output:
Roll Number: 0
Name: unnamed
Marks: 0
Grade: N/A
--------------------
Roll Number: 21
Name: Meera
Marks: 88
Grade: A"""
class Student: 
    def __init__(self): 
        self.roll_number = 0 
        self.name = "unnamed"
        self.marks = 0
        self.grade = "N/A"

    def display(self): 
        print(f"Roll Number: {self.roll_number}")
        print(f"Name: {self.name}")
        print(f"Marks: {self.marks}")
        print(f"Grade: {self.grade}")

student = Student() 
print("Enter you're Details Below: ")
roll_number = int(input("Roll Number: "))
name = input("Name: ")
marks = int(input("Marks: "))
grade = input("Grade: ")

# printing default values 
student.display()

# Assigning values to student object 
student.roll_number = roll_number
student.name = name 
student.marks = marks 
student.grade = grade

print("-"*20)
# printing student details 
student.display() 
