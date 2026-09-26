while True: 
    print("Movie Management System")
    options = """Options: 
    1. Add a Movie 
    2. Display a Movie 
    3. Display all Movies 
    4. Delete a Movie 
    5. Exit"""
    print(options)
    choice = int(input("Enter your choice: "))
    match choice: 
        case 1: 
            print("Adding a Movie: ")
        case 2: 
            print("Displaying a Movie: ")
        case 3: 
            print("Displaying all Movies: ")
        case 4: 
            print("Deleting a Movie: ")
        case 5: 
            print("Exiting...")
        case _ : # whenever user eneter a invalid value you go here 
            print("Invalid choice")