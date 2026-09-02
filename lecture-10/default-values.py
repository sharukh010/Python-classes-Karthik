def display(first_name: str,last_name: str | None = None ): 
    print(f"First Name: {first_name}")
    if last_name != None: 
        print(f"Last Name: {last_name}") 
display("karthik","veli")