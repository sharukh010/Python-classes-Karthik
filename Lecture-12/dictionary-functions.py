sample = {"a":1,"b":2}
# print(sample["c"]) # this is not a safe way to access dictionary keys 
#1. get function 
# print(sample.get("c")) # returns None 
marks = sample.get("c",0)
print(marks + 1)

copy = sample.copy() # copy of sample dictionary 

students = ["Arjun","Vibha","Karthik","Joe"]
marks = dict.fromkeys(students,100)
# print(marks)

# print(marks.items()) # return key,value pairs 
# print(marks.values())
# print(marks.keys())
# marks.clear() # this removes all the elments inside a dictionary
# print(marks)
# print(marks.pop("Joe"))
# print(marks)
# print(marks.popitem())
# print(marks)
# marks.update({"Joe":75})
# *args -> tuple of values 
# **kwargs -> dictionary 
# marks.update(Joe=75)
# marks.update(Kiran=98)
print(marks.setdefault("Sneha",80))
print(marks)