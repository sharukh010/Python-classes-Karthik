import tabulate
def get_student(sid:int)->dict[str]: 
    for student in students: 
        if student["id"] == sid: 
            return student 
    print("get_student: Student Not found")
    return None 

def add_student(student:dict[str]): 
    students.append(student)

def delete_student(sid:int): 
    student = get_student(sid)
    if student == None: 
        print("delete_student: Cannot Delete Student Details")
    else: 
        students.remove(student)
        print("Succesfully Deleted student details")

def display_student(sid:int): 
    student = get_student(sid)
    if student == None: 
        print("display_student: no data")
    else: 
       table = tabulate.tabulate([student],headers="keys",tablefmt="grid")
       print(table)

def update_student(sid: int, key: str,value: str | int): 
    student = get_student(sid)
    allowed_keys = ["name","age","dob","grade","gender"]
    if student == None: 
        print("update_student: no data")
    else:
        if key in allowed_keys: 
            student[key] = value 
        else: 
            print(f"update_student: cannot edit {key}")



students = [] 
sid = 1 
options = """Options: 
1. Add a student 
2. Delete a Student 
3. Display a Student 
4. Update a Student Details 
5. Quit 
"""


while True: 
    print(options)
    choice  = int(input("Enter your choice (1-5): "))
    match choice: 
        case 1:
            print("Adding Student: ")
            name = input("Name: ")
            age = int(input("Age: "))
            dob = input("DOB (dd/mm/yyyy): ")
            gender = input("Gender: ")
            grade = input("Grade: ")
            school = "TridaPro"
            student = {
                "id": sid,# should not be updated
                "name":name,
                "age": age,
                "dob": dob,
                "gender": gender,
                "grade": grade,
                "school": school #should not be updated 
            }
            # here the implementation of add_student 
            # will not effect the program 
            # this concept is called as abstraction 
            # where the implementation is hidden from the user 
            add_student(student)
            sid += 1 

        case 2:
            print("Deleting Student: ")
            target_id = int(input("ID: "))
            delete_student(target_id)
        case 3: 
            print("Displaying Student: ")
            target_id = int(input("ID: "))
            display_student(target_id)
        case 4: 
            print("Updating Student: ")
            target_id = int(input("ID: "))
            print("Options:\n1. Name\n2. Age\n3. Date of Birth\n4. Gender\n5. Grade")
            edit_choice = int(input("Enter your choice (1-5): "))
            match edit_choice:
                case 1: 
                    name = input("Enter the updated Name: ")
                    update_student(target_id,"name",name)
                case 2:
                    age = int(input("Enter the updated Age: "))
                    update_student(target_id,"age",age)
                case 3: 
                    dob = input("Enter the updated DOB(DD-MM-YYYY): ")
                    update_student(target_id,"dob",dob)
                case 4: 
                    gender = input("Enter the updated Gender: ")
                    update_student(target_id,"gender",gender)
                case 5: 
                    grade = input("Enter the updated Grade: ")
                    update_student(target_id,"grade",grade)
                case _ : 
                    print("Invalid choice, Try again")
        case 5: 
            print("Quitting...")
            break 
    confirmation = input("Do you want to continue (y/n)? ")
    if confirmation == "y": 
        continue 
    else: 
        print("Quitting...")
        break 