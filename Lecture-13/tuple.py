"""
Tuple is similar to list in terms storing and accessing data 
but the difference is 
tuple is immutable (changed)
no adding elements possible 
"""
grades = ("A-","A","A+","B-","B","B+","C-","C","C+","D-","D","D+","E-","E","E+","F-","F","F+")
# print(grades[0])
# grades[0] = "G+" # you cannot update it's value 


# How to modify a tuple? 
grades = list(grades)
grades.extend(["G-","G","G+"])
grades = tuple(grades)

grades = list(grades)
grades.remove("G")
grades = tuple(grades)