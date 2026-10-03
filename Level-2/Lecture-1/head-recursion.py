def display(n): 
    if n == 0: 
        return 
    else: 
        display(n-1)
        print(n)

display(10)