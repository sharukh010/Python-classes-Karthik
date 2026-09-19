import turtle as t 
def find_person(target_id): 
    target = None 
    for person in persons: 
        if person["id"] == target_id: 
            target = person 
            break 
    return target 
persons = [
    {
        "id":1,
        "name":"karthik",
        "age":14
    }
] 

options="""Options: 
1. Add Person Details
2. Show Person Details
"""
pid = 1 
while True: 
    choice = int(t.textinput("P.M.S",options))
    match choice: 
        case 1: 
            name = "" 
            while name == "" or name == None: 
                name = t.textinput("Add Person","Enter your Name: ")
            age = None 
            while age == None: 
                age = t.numinput("Add Person","Enter you Age: ")
            age = int(age)
            pid += 1 
            person = {"id":pid,"name":name,"age": age}
            persons.append(person.copy())
            message = f"Person with ID {pid} is added"
            response = t.textinput("Response",f"{message}.\nDo you want to continue (y/n) ?")
            if response == "y": 
                continue 
            else: 
                break 
        case 2: 
            target_id = t.numinput("Display Person","Enter Person ID: ")
            target_id = int(target_id)
            person = find_person(target_id)
            if person == None: 
                message = f"Person with ID {target_id} is not found"
                response = t.textinput("Response",f"{message}.\nDo you want to continue (y/n) ?")
                if response == "y": 
                    continue 
                else: 
                    break 
            else: 
                data = f"""ID: {person["id"]}\nName: {person["name"]}\nAge: {person["age"]}"""
                response = t.textinput("Response",f"Person Details:\n{data}.\nDo you want to continue (y/n) ?")
                if response == "y": 
                    continue 
                else: 
                    break 