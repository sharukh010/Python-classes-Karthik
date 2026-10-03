def complete_mission_nt(clone_number,curr_distance,total_distance):
    # the condition at which you will stop the recursion is called 
    # base condition 
    if curr_distance > total_distance: 
        print("Nine Tail found")
        return 
    else: 
        # this condition is called 
        # recursive condition 
        print(f"Clone-{clone_number} is calling for Clone-{clone_number+1}")
        complete_mission_nt(clone_number+1,curr_distance+5,total_distance)
        print(f"Message passed from Clone-{clone_number+1} to Clone-{clone_number}")
# recursion can almost do what a loop can do 
# but you cannot do everything that you do with recursion using loops 
complete_mission_nt(0,0,50)